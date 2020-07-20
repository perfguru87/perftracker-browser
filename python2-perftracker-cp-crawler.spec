%define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")
%define _perftracker_lib_ver 0.1.3
%define _perftracker_cp_crawler_ver 0.1.3

Name:		python2-perftracker-cp-crawler
Version:	%{_perftracker_cp_crawler_ver}
Release:	0
Summary:	The perftracker web UI Control Panels crawler libraries

BuildArch:	noarch
Group:		Development/Libraries
License:	MIT

BuildRequires:	python
Requires:	epel-release python python2-pip python-devel python-dateutil python2-perftracker-lib git gcc
Requires:       xorg-x11-server-Xvfb chromedriver google-chrome-stable libjpeg-devel zlib-devel

%description
A set of libraries and scripts to crawl web UI Control Panels (like Wordpress), integrated with client library for the perftracker:
https://github.com/perfguru87/perftracker

%install
mkdir $RPM_BUILD_ROOT/bin
touch $RPM_BUILD_ROOT/bin/pt-wp-crawler.py

%post
echo -e "\n====== Installing the perftracker-cp-crawler v%{_perftracker_cp_crawler_ver} from sources =======\n"
echo "pip2 install --upgrade perftracker-cp-crawler=%{_perftracker_lib_ver}"
pip2 install --upgrade perftracker-cp-crawler=%{_perftracker_lib_ver}
echo -e "\n====== The perftracker-lib installation done ======================\n"

%postun
echo -e "\n====== Uninstalling the perftracker-cp-crawler v%{_perftracker_cp_crawler_ver} =======\n"
echo "pip2 uninstall -y perftracker-cp-crawler=%{_perftracker_lib_ver}"
pip2 uninstall -y perftracker-cp-crawler=%{_perftracker_lib_ver}
echo -e "\n====== The perftracker-cp-crawler uninstallation done =========\n"

%files

%ghost
/bin/pt-wp-crawler.py

%changelog
* Mon Jul 20 2020 <perfguru87@gmail.com>
- require python2-pip
* Sat Jul 18 2020 <perfguru87@gmail.com>
- initial version
