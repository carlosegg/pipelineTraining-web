Name:      web
Summary:   Pipeline training web
Version:   %{versionModule}
Release:   %{releaseModule}
License:   GPL 3.0
Packager:  ss
Vendor:    softwaresano
Group:     pipeline
BuildArch: noarch

Requires:  httpd >= 2.2
%define prefix_organization ss
%define package_name web
%define _prefix_   %{_usr}/local
%define project_user %{package_name}
%define component_home /etc/%{prefix_organization}/%{_project_name}/pipelineTraining 
%define web_home /opt/%{prefix_organization}/%{_project_name}/web/pipelineTraining/



%description
Pipeline training web.

%prep

_log "Building package %{name}-%{version}-%{release}"
[ -d $RPM_BUILD_ROOT/%{component_home} ] || %{__mkdir_p} $RPM_BUILD_ROOT/%{component_home}
[ -d $RPM_BUILD_ROOT/%{web_home} ] || %{__mkdir_p} $RPM_BUILD_ROOT/%{web_home}/


%build


%install
if [ -d "%{_sourcedir}/pipelineTraining" ]; then
   %{__cp} -R %{_sourcedir}/pipelineTraining/* ${RPM_BUILD_ROOT}/%{component_home}
fi


%{__cp} -R "%{_srcrpmdir}/../target/site/"* "$RPM_BUILD_ROOT/%{web_home}/" 

%clean 
[ ${RPM_BUILD_ROOT} != "/" ] && rm -rf ${RPM_BUILD_ROOT}/*

%files
%attr (-,%{project_user},%{project_user}) /%{web_home}/
%config %attr (-,%{project_user},%{project_user}) %{component_home}

%pre

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

