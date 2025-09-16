######################
# Hardcode PLF build
%define	build_plf 0
######################

%if %{build_plf}
%define	distsuffix plf
# make EVR of plf build higher than regular to allow update, needed with rpm5 mkrel
%define	extrarelsuffix plf
%endif

%define		_kde6_services	%{_datadir}/kio/servicemenus
%define		_kde6_appsdir	%{_datadir}/apps

Summary:	An audio converter
Name:	audiokonverter
Version:	6.0.0
Release:	2%{?extrarelsuffix}
License:	GPLv2+
Group:	Sound
Url:		https://store.kde.org/p/998467/
Source0:	%{name}-%{version}.tar.bz2
Source100:	audiokonverter.rpmlintrc
Patch0:	audiokonverter-6.0.0-drop-Encoding-from-desktop-files.patch
#	TODO: provide apetag, musepack-tools (mpcdec) and replaygain
# Main dep
Requires:	plasma6-dolphin
# Deps for various options
%if %{build_plf}
Requires:	faac
Requires:	faad2
%endif
Requires:	flac
Requires:	ffmpeg
Requires:	id3lib
Requires:	lame
Requires:	mplayer
Requires:	vorbis-tools
Requires:	wavpack
# This is in NonFree
Recommends:	shorten
BuildArch:	noarch

%description
A small utility to easily convert from OGG, MP3, AAC, M4A, FLAC, WMA,
RealAudio, Musepack, Wavpack, WAV and movies to MP3, OGG, M4A, WAV and FLAC
in Dolphin by right-clicking on them.
%if %{build_plf}
This package is in restricted because it requires packages that are in
restricted (faac, faad2).
%endif

%files
%license COPYING
%doc README Changelog
%{_bindir}/*
%{_kde6_services}/*.desktop

#-----------------------------------------------------------------------------

%prep
%autosetup -p1


%build
# Only scripts: nothing to do.


%install
mkdir -p %{buildroot}%{_kde6_services}
install -m 755 *5.desktop %{buildroot}%{_kde6_services}
install -m 755 Oggdrop-Lx.desktop %{buildroot}%{_kde6_services}
mkdir -p %{buildroot}%{_bindir}
install -m 755 anytowav5 audioconvert5 movie2sound5 oggdrop-lx %{buildroot}%{_bindir}
