%define	name	x2vnc
%define	version	1.7.2
%define	release	%mkrel 3

Summary:	Allows a mouse and a keyboard to control two displays
Name:		%{name}
Version:	%{version}
Release:	%{release}
URL:		http://fredrik.hubbe.net/x2vnc.html
Source0:	http://fredrik.hubbe.net/x2vnc/%{name}-%{version}.tar.bz2
Group:		System/X11
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:	BSD
BuildRequires:	X11-devel

%description
x2vnc allows the keyboard and mouse on one ("from") X display to control 
another ("to") VNC display.

%prep
%setup -q

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}/%{_mandir}
%makeinstall_std
#%{__install} -m755 %{name} -D $RPM_BUILD_ROOT%{_bindir}/%{name}
#%{__install} -m644 %{name}.man -D $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr (-,root,root)
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

