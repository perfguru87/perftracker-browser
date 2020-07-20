%define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")
%define _perftracker_lib_ver 0.1.0
%define _perftracker_cp_crawler_ver 0.1.0

Name:		perftracker-cp-crawler
Version:	%{_perftracker_cp_crawler_ver}
Release:	0
Summary:	The perftracker web UI Control Panels crawler libraries

BuildArch:	noarch
Group:		Development/Libraries
License:	MIT

BuildRequires:	python
Requires:	python git gcc python-devel python-setuptools python-dateutil
Requires:       xorg-x11-server-Xvfb chromedriver google-chrome-stable libjpeg-devel zlib-devel

%description
A set of libraries and scripts to crawl web UI Control Panels (like Wordpress), integrated with client library for the perftracker:
https://github.com/perfguru87/perftracker

%install
mkdir $RPM_BUILD_ROOT/bin
touch $RPM_BUILD_ROOT/bin/pt-wp-crawler.py

%post
echo -e "\n====== Installing the perftracker-lib v%{_perftracker_lib_ver} from sources =======\n"
echo "PRE easy_install git+https://github.com/perfguru87/perftracker-lib.git@v%{_perftracker_lib_ver}"
easy_install git+https://github.com/perfguru87/perftracker-lib.git@v%{_perftracker_lib_ver} || exit -1
echo -e "\n====== The perftracker-lib installation done ======================\n"
echo -e "\n====== Installing the perftracker-cp-crawler v%{_perftracker_cp_crawler_ver} from sources =======\n"
echo "PRE easy_install git+https://github.com/perfguru87/perftracker-cp-crawler.git@v%{_perftracker_cp_crawler_ver}"
easy_install git+https://github.com/perfguru87/perftracker-lib.git@v%{_perftracker_cp_crawler_ver} || exit -1
echo -e "\n====== The perftracker-lib installation done ======================\n"

%postun
echo -e "\n====== Uninstalling the perftracker-lib v%{_perftracker_lib_ver} =======\n"
echo "rm -rf %{python_sitelib}/perftrackerlib-%{_perftracker_lib_ver}*.egg"
rm -rf "%{python_sitelib}/"perftrackerlib-%{_perftracker_lib_ver}*.egg
echo -e "\n====== The perftracker-lib uninstallation done =========\n"
echo -e "\n====== Uninstalling the perftracker-cp-crawler v%{_perftracker_cp_crawler_ver} =======\n"
echo "rm -rf %{python_sitelib}/perftrackerlib-%{_perftracker_cp_crawler_ver}*.egg"
rm -rf "%{python_sitelib}/"perftrackerlib-%{_perftracker_cp_crawler_ver}*.egg
echo -e "\n====== The perftracker-cp-crawler uninstallation done =========\n"

%files

%ghost
/bin/pt-wp-crawler.py

%changelog
* Sat Jul 18 2020 <perfguru87@gmail.com>
- initial version
