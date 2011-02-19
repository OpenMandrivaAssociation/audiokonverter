%define name    audiokonverter
%define pre   	0
%define version 5.9.1
%define rel	1
%if %pre
%define release	%mkrel -c %pre %rel
%define tarver	%version-%pre
%else
%define release	%mkrel %rel
%define tarver	%version
%endif

%define iconname %{name}.png
%define build_plf 0

%bcond_with plf
%if %with plf
%define build_plf 1
%define distsuffix plf
%if %mdvver >= 201100
# make EVR of plf build higher than regular to allow update, needed with rpm5 mkrel
%define extrarelsuffix plf
%endif
%endif

Summary:	An audio converter
Name:		%{name}
Version:	%{version}
Release:	%{release}%{?extrarelsuffix}
License:	GPLv2
Group:		Sound
Source0:	http://www.kde-apps.org/CONTENT/content-files/12608-%name-%tarver.tar.bz2
URL:		http://www.kde-apps.org/content/show.php?content=12608
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	kde4-macros
Requires:	dolphin
Requires:	mplayer flac wavpack
Requires:	id3lib vorbis-tools 
BuildArch:	noarch

%if %build_plf
Requires:	lame faac faad2
%else
Patch0:		audiokonverter-noflac.patch 
%endif

%description 
audiokonverter is a small utility to easily convert from OGG, MP3,
AAC, M4A, FLAC, WMA, RealAudio, Musepack, Wavpack, WAV and movies to
MP3, OGG, M4A, WAV and FLAC in Konqueror by right-clicking on them.

%if %build_plf
This package is in PLF because it requires packages that are in PLF.
%endif

%prep
%setup -q -n %{name}-%{tarver}
%if !%build_plf
%patch0 -p0 -b .plf
%endif
 
%install
rm -f %buildroot
mkdir -p %{buildroot}%_kde_services/ServiceMenus
install -m 644 *4.desktop %{buildroot}%_kde_services/ServiceMenus
mkdir -p %{buildroot}%_kde_appsdir/dolphin/servicemenus
install -m 644 *4.desktop %{buildroot}%_kde_appsdir/dolphin/servicemenus
mkdir -p %{buildroot}%_kde_bindir
install -m 755 anytowav4 audioconvert4 movie2sound4 oggdrop-lx %buildroot%_kde_bindir

%clean 
rm -rf %{buildroot}

%files
%defattr (-,root,root)
%doc README Changelog
%_kde_bindir/*
%_kde_services/ServiceMenus/*.desktop
%_kde_appsdir/dolphin/servicemenus/*.desktop
