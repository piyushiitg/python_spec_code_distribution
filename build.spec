
 
Example:
 
%define build_no 1
Name: Diagnostic_Setup
Version: 1.0
Release: %{build_no}
Summary: Test Diagnostics
License: Test Proprietary
Group: Test
BuildRoot: %{_topdir}/BUILDROOT/%{name}-%{version}.%{_arch}
Packager: TUSHAR RAUT <singhai.piyush@gmail.com>
Summary: Test utilities
Source: %{name}.tar.gz
Requires: python>=2.6
Vendor: Test Inc.
 
#BuildRequires:
 
%description
Test utilities
 
%prep
##%setup -q
cd %{_topdir}/BUILD
gzip -cd %{_topdir}/SOURCES/%{name}.tar.gz | tar xvf -
%build
echo "No build required"
 
%install
cd %{_topdir}/BUILD/%{name}-%{version}
mkdir -p %{buildroot}/opt/idb/diagnostic
mkdir -p %{buildroot}/opt/idb/diagnostic/logs
mkdir -p %{buildroot}/opt/idb/diagnostic/packetdump
mkdir -p %{buildroot}/opt/idb/diagnostic/logs/bin/
mkdir -p %{buildroot}/opt/idb/diagnostic/packetdump/bin/
mkdir -p %{buildroot}/usr/lib64/python2.6/site-packages/diag_comm
cp logs/Global_variables.py %{buildroot}/usr/lib64/python2.6/site-packages/diag_comm
cp logs/__init__.py %{buildroot}/usr/lib64/python2.6/site-packages/diag_comm
cp logs/Logs_stat.py %{buildroot}/usr/lib64/python2.6/site-packages/diag_comm
cp -rf logs/Other_logs %{buildroot}/usr/lib64/python2.6/site-packages/diag_comm
cp -rf logs/Query_logs %{buildroot}/usr/lib64/python2.6/site-packages/diag_comm
 
sudo pip install dpkt
sudo pip install enum
sudo yum install wireshark
 
%files
%dir /usr/lib64/python2.6/site-packages/diag_comm/Other_logs
%dir /usr/lib64/python2.6/site-packages/diag_comm/Query_logs
%defattr(644,root,root)
%attr(644,root,root) /usr/lib64/python2.6/site-packages/diag_comm/Global_variables.py
%attr(644,root,root) /usr/lib64/python2.6/site-packages/diag_comm/__init__.py
%attr(644,root,root) /usr/lib64/python2.6/site-packages/diag_comm/Logs_stat.py
%attr(644,root,root) /opt/idb/diagnostic/logs/bin/main_logs.py
%attr(644,root,root) /opt/idb/diagnostic/packetdump/bin/main_mssql.py
%attr(644,root,root) /opt/idb/diagnostic/packetdump/bin/main_mysql.py
%attr(644,root,root) /opt/idb/diagnostic/packetdump/bin/main_oracle.py
 
%clean
 
