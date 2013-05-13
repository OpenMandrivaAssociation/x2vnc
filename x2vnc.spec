%define	name	x2vnc
%define	version	1.7.2
%define release 	7

Summary:	Allows a mouse and a keyboard to control two displays
Name:		%{name}
Version:	%{version}
Release:	%{release}
URL:		http://fredrik.hubbe.net/x2vnc.html
Source0:	http://fredrik.hubbe.net/x2vnc/%{name}-%{version}.tar.bz2
Patch0:		x2vnc-1.7.2-fix-str-fmt.patch
Group:		System/X11
License:	BSD
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xinerama)
BuildRequires:	pkgconfig(xrandr)
BuildRequires:	pkgconfig(xscrnsaver)
BuildRequires:	pkgconfig(xxf86dga)

%description
x2vnc allows the keyboard and mouse on one ("from") X display to control 
another ("to") VNC display.

%prep
%setup -q
%patch0 -p0

%build
%configure2_5x
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



%changelog
* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 1.7.2-6mdv2011.0
+ Revision: 615468
- the mass rebuild of 2010.1 packages

* Sun Feb 21 2010 Funda Wang <fwang@mandriva.org> 1.7.2-5mdv2010.1
+ Revision: 508919
- fix str fmt

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Sun Aug 03 2008 Thierry Vignaud <tv@mandriva.org> 1.7.2-4mdv2009.0
+ Revision: 262222
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.7.2-3mdv2009.0
+ Revision: 256489
- rebuild
- fix no-buildroot-tag

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 1.7.2-1mdv2008.1
+ Revision: 129794
- kill re-definition of %%buildroot on Pixel's request
- import x2vnc


* Wed Sep 06 2006 Buchan Milne <bgmilne@mandriva.org> 1.7.2-1mdv2007.0
- New release 1.7.2

* Tue May 23 2006 Lenny Cartier <lenny@mandriva.com> 1.7.1-1mdk
- 1.7.1

* Tue Sep 06 2005 Buchan Milne <bgmilne@linux-mandrake.com> 1.6.1-2mdk
- annual rebuild
- fix group/buildrequires, url, source url

* Wed Sep 02 2004 Buchan Milne <bgmilne@linux-mandrake.com> 1.6.1-1mdk
- 1.6.1

* Mon Jun 07 2004 Buchan Milne <bgmilne@linux-mandrake.com> 1.6-1mdk
- First Mandrake package
