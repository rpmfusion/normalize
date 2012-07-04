%define plugindir %(xmms-config --effect-plugin-dir 2>/dev/null)

Summary:  Tool for adjusting the volume of audio files to a standard level
Name:     normalize
Version:  0.7.7
Release:  7%{?dist}
URL:      http://normalize.nongnu.org/
License:  GPLv2+
Group:    Applications/Multimedia
Source:   http://savannah.nongnu.org/download/normalize/normalize-0.7.7.tar.bz2
BuildRoot:  %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires:  audiofile-devel >= 1:0.2.1-2, libmad-devel
BuildRequires:  gettext
# Binaries from the following are required. 
BuildRequires:  lame, vorbis-tools
# Explicit, because won't be detected automatically.
Requires:  lame, vorbis-tools
%ifarch x86_64
BuildRequires:  libtool 
%endif

%description
normalize is a tool for adjusting the volume of audio files to a
standard level. This is useful for things like creating mixed CDs
and mp3 collections, where different recording levels on different
albums can cause the volume to vary greatly from song to song.

%package -n xmms-%{name}
Summary:  Relative volume adjustment plugin for XMMS
Group:    Applications/Multimedia
BuildRequires:  xmms-devel, gtk+-devel
Requires:  xmms-libs, %{name} = %{version}-%{release}

%description -n xmms-%{name}
Plugin for XMMS to honour relative volume adjustment (RVA2) ID3 tag frames.


%prep
%setup -q


%build
%configure --enable-xmms --with-mad --with-audiofile
make  \
%ifarch x86_64
  LIBTOOL=/usr/bin/libtool \
%endif
  %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
%find_lang %{name}


%clean
rm -rf $RPM_BUILD_ROOT


%files -f %{name}.lang
%defattr(-,root,root)
%doc COPYING README NEWS THANKS TODO
%{_bindir}/normalize
%{_bindir}/normalize-mp3
%{_bindir}/normalize-ogg
%{_mandir}/man1/normalize.1.gz
%{_mandir}/man1/normalize-mp3.1.gz


%files -n xmms-%{name}
%defattr(-,root,root)
%{plugindir}/librva.so
%exclude %{_libdir}/xmms/Effect/librva.*a
# The * here is for x86_64 build where a librva.a and a librva.la are builded

%changelog
* Wed Jul 04 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.7.7-7
- Rebuilt - missing mass rebuilt

* Wed Jan 25 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.7.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 0.7.7-5
- rebuild for new F11 features

* Mon Aug 04 2008 David Timms <iinet.net.au [AT] dtimms> 0.7.7-4
- mod BR: to libmad, del Requires: mad

* Sun Aug 03 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 0.7.7-3
- rebuild

* Fri Oct 06 2006 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> 0.7.7-2
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Sun Sep 24 2006 Michael Schwendt <mschwendt[AT]users.sf.net> - 0.7.7-1
- Update to 0.7.7 (new upstream locations).

* Fri Apr  7 2006 Dams <anvil[AT]livna.org> - 0.7.6-11
- xmms package requires xmms-libs instead of xmms

* Mon Mar 13 2006 Thorsten Leemhuis <fedora[AT]leemhuis.info> 0.7.6-10
- Drop Epoch completely

* Thu Mar 09 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- switch to new release field
- drop Epoch

* Tue Feb 28 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- add dist

* Fri Dec 31 2004 Thorsten Leemhuis <fedora[AT]leemhuis[DOT]info> 0:0.7.6-0.lvn.9
- fix x86_64 build; inside mach the integrated libtool does not work

* Thu May 20 2004 Dams <anvil[AT]livna.org> - 0:0.7.6-0.lvn.8
- xmms-config errors redirected to dev/null

* Sun May  4 2003 Michael Schwendt <mschwendt[AT]users.sf.net> - 0:0.7.6-0.fdr.7
- Use $RPM_BUILD_ROOT instead of %{buildroot}.
- Fix spec file in accordance with bug #213 comments #14 and #15.

* Sun Apr 27 2003 Michael Schwendt <mschwendt[AT]users.sf.net>
- Rename package normalize-xmms to xmms-normalize.
- Use explicit Epoch 1 for versioned audiofile, drop version
  requirement for xmms.

* Sat Apr 26 2003 Michael Schwendt <mschwendt[AT]users.sf.net>
- Drop explicit Requires where possible.
- Update for split "mad" packages (bug #187).

* Fri Apr 25 2003 Michael Schwendt <mschwendt[AT]users.sf.net>
- Update spec file according to Fedora package request bug #213.

* Sat Apr  5 2003 Michael Schwendt <mschwendt[AT]users.sf.net>
- Depend on libmad-*.
- RHL9 build.

* Sun Apr 14 2002 Michael Schwendt <mschwendt[AT]users.sf.net>
- Initial RPM built for Red Hat Linux 7.2.
- Wants libaudiofile >= 0.2.2, but 0.2.1-2 seems to work.
  and passes tests, too.
- Descriptions taken from Chris Vaill's spec file.

