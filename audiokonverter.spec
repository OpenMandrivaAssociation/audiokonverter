%define name    audiokonverter
%define pre   	%nil
%define version 5.5.1
%define release %mkrel 3

%define iconname %{name}.png
%define build_plf 0

Summary:	An audio converter
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Sound
Source0:	%{name}-%{version}%{pre}.tar.bz2
URL:		http://www.kde-apps.org/content/show.php?content=12608
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	kdebase-progs
Requires:	mplayer flac wavpack
Requires:	id3lib vorbis-tools 
BuildArch:	noarch

%if %build_plf
%define distsuffix plf
Requires:	lame faac faad2 
%else
Patch0:		audiokonverter-noflac.patch
%endif

%description 
audiokonverter is a small utility to easily convert from OGG, MP3,
AAC, M4A, FLAC, WMA, RealAudio, Musepack, Wavpack, WAV and movies to
MP3, OGG, M4A, WAV and FLAC in Konqueror by right-clicking on them.

%prep
%setup -q -n %{name}-%{version}%{pre}
%if !%build_plf
%patch0 -p1 -b .nolame
%endif
 
%install
mkdir -p %{buildroot}%{_bindir}
install -m755 anytowav audioconvert movie2sound %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/apps/konqueror/servicemenus/
install -m 644 audioconvert.desktop audiofrommovie.desktop %{buildroot}%{_datadir}/apps/konqueror/servicemenus/

%clean 
rm -rf %{buildroot}

%files
%defattr (-,root,root)
%doc README Changelog
%{_bindir}/* 
%{_datadir}/apps/konqueror/servicemenus/


