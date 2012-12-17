Summary:	Port to Qt of Neil Hodgson's Scintilla C++ editor control
Name:		qscintilla
Version:	2.7
Release:	1
License:	GPL v2 or GPL v3 with Riverbank GPL Exception v1.1
Group:		X11/Libraries
Source0:	http://downloads.sourceforge.net/pyqt/QScintilla-gpl-%{version}.tar.gz
# Source0-md5:	a3857d75a2b332e0460131e0aa4cc4b5
URL:		http://www.riverbankcomputing.co.uk/software/qscintilla/
BuildRequires:	QtGui-devel
BuildRequires:	qt-build
BuildRequires:	qt-qmake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A port to Qt of Neil Hodgson's Scintilla C++ editor control.

%package devel
Summary:	Development files for the QScintilla
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	QtGui-devel

%description devel
Development files for the QScintilla.

%prep
%setup -qn QScintilla-gpl-%{version}

%build
cd Qt4Qt5
qmake qscintilla.pro
%{__make}
cd -

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C Qt4Qt5 install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%find_lang %{name} --without-mo --with-qm

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc GPL_EXCEPTION.TXT NEWS OPENSOURCE-NOTICE.TXT README
%attr(755,root,root) %ghost %{_libdir}/libqscintilla2.so.9
%attr(755,root,root) %{_libdir}/libqscintilla2.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libqscintilla2.so
%{_includedir}/qt/Qsci

