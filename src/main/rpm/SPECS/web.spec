Name:      web
Summary:   Pipeline training web
Version:   %{versionModule}
Release:   %{releaseModule}
License:   GPL 3.0
Packager:  pdi
Vendor:    tid.es
Group:     pipeline
BuildArch: noarch

Requires:  httpd >= 2.2
%define prefix_organization pdi
%define package_name web
%define _prefix_   %{_usr}/local
%define project_user %{package_name}
%define component_home /etc/%{prefix_organization}/%{_project_name}/pipelineTraining 
%define web_home /opt/%{prefix_organization}/%{_project_name}/web/pipelineTraining/
%define pipeline_home /opt/pipeline/%{prefix_organization}/%{_project_name}/enviroment
%define enviroments_dir /var/tmp/%{package_name}/enviroments
%define source_enviroments_dir %{_sourcedir}/pipeline_training/../enviroments


%description
Pipeline training web

%prep

_log "Building package %{name}-%{version}-%{release}"
[ -d $RPM_BUILD_ROOT/%{component_home} ] || %{__mkdir_p} $RPM_BUILD_ROOT/%{component_home}
[ -d $RPM_BUILD_ROOT/%{enviroments_dir} ] || %{__mkdir_p} $RPM_BUILD_ROOT/%{enviroments_dir}
[ -d $RPM_BUILD_ROOT/%{web_home} ] || %{__mkdir_p} $RPM_BUILD_ROOT/%{web_home}/


%build


%install
if [ -d "%{_sourcedir}/pipelineTraining" ]; then
   %{__cp} -R %{_sourcedir}/pipelineTraining/* ${RPM_BUILD_ROOT}/%{component_home}
fi

if [ -d "%{source_enviroments_dir}" ]; then
   %{__cp} -R %{source_enviroments_dir}/* ${RPM_BUILD_ROOT}/%{enviroments_dir}
fi

%{__cp} -R "%{_srcrpmdir}/../target/site/"* "$RPM_BUILD_ROOT/%{web_home}/" 

%clean 
[ ${RPM_BUILD_ROOT} != "/" ] && rm -rf ${RPM_BUILD_ROOT}/*

%files
%attr (-,%{project_user},%{project_user}) /%{web_home}/
%config %attr (-,%{project_user},%{project_user}) %{component_home}
%config %attr (-,%{project_user},%{project_user}) %{enviroments_dir}

%pre
enviroment=`cat %{pipeline_home}`
if [ "$?" != 0 ]; then
   _log "[ERROR] Esta máquina no está dentro del pipeline"
   exit 1
fi

[ "`grep \"^%{project_user}:\" /etc/passwd`" == "" ] && useradd %{project_user}
sed -i s:"/home/%{project_user}\:/bin/sh":"/sbin/nologin\:/bin/bash":g /etc/passwd
_log "Parando apache" 
service httpd stop 

%post
enablePorts(){
   if [ -f "/etc/sysconfig/iptables" ]; then
      HTTP_PORT=80
      isRHFirewall=`cat /etc/sysconfig/iptables|grep "\-A RH-Firewall"`
      if ! [ -z $isRHFirewall ]; then 
         ENABLED_HTTP_PORT=`cat /etc/sysconfig/iptables|grep "\-A RH-Firewall-1-INPUT -p tcp -m state --state NEW -m tcp --dport ${HTTP_PORT} -j ACCEPT"`
      if [ "$ENABLED_HTTP_PORT" == "" ]; then
         sed -i s:"-A RH-Firewall-1-INPUT -m state --state NEW -m tcp -p tcp --dport 22 -j ACCEPT":"-A RH-Firewall-1-INPUT -m state --state NEW -m tcp -p tcp --dport 22 -j ACCEPT\n-A RH-Firewall-1-INPUT -p tcp -m state --state NEW -m tcp --dport ${HTTP_PORT} -j ACCEPT":g /etc/sysconfig/iptables
         /sbin/service iptables restart
      fi
      else 
         ENABLED_HTTP_PORT=`cat /etc/sysconfig/iptables|grep "\-A INPUT -p tcp -m state --state NEW -m tcp --dport ${HTTP_PORT} -j ACCEPT"`
         if [ "$ENABLED_HTTP_PORT" == "" ]; then
            sed -i s:" --dport 22 -j ACCEPT":" --dport 22 -j ACCEPT\n-A INPUT -p tcp -m state --state NEW -m tcp --dport ${HTTP_PORT} -j ACCEPT":g /etc/sysconfig/iptables
         /sbin/service iptables restart
         fi
      fi
   fi
}
enviroment=`cat %{pipeline_home}`
#Si se trata de una configuración específica del entorno,
#se borra la configuración por defecto y se copia la configuración específica
if [ -d "%{enviroments_dir}/${enviroment}" ]; then
   _log "Personalizando el entorno de [${enviroment}]"
   %{__cp} -R %{enviroments_dir}/${enviroment}/* %{component_home}/
fi
rm -Rf %{enviroments_dir}

rm -Rf "/var/www/%{_project_name}"
ln -s "%{web_home}" "/var/www/%{_project_name}"

cd "/etc/httpd/conf.d/"
rm -Rf pipelineTraining.conf
ln -s "%{component_home}/pipelineTraining.conf" .
chcon -Rv --type=httpd_sys_content_t "%{web_home}"
#Redirect apache tomcat
/usr/sbin/setsebool -P httpd_can_network_connect 1 
_log "Starting apache"
service httpd start
_log "Habilitando acceso a Apache"
enablePorts
%preun
_log "Shutdown apache" 
service httpd stop 

%postun
_log "Starting apache" 
service httpd start 

