Summary:	Beneath a Steel Sky
Name:		bass
Version:	1.0
Release:	1
License:	Freeware (not sure about manual and comics)
Group:		Applications/Games
Source0:	http://dl.sf.net/scummvm/BASS-CD.zip
# Source0-md5: 18f9045e90d56fdfc3263b7f264791fd
Source1:	http://www.the-underdogs.org/games/b/bass/files/%{name}.pdf
Source2:	http://www.the-underdogs.org/games/b/bass/files/%{name}-comics.zip
URL:		http://www.revolution.co.uk/_display.php?id=16
Requires:	scummvm >= 0.5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
After the Dungeons and Dragons fantasy setting of Revolution's first
game, Lure of the Temptress, Revolution decided to go down a
completely different avenue with its second adventure game, Beneath a
Steel Sky, that of Science Fiction. A bleak vision of the future was
imagined, where mind control and medical science combined forces to
repress the populace. Leading comic artist, Dave Gibbons, joined the
design team to visualise this desperate landscape. The result,
released in 1994, was the cult classic Beneath a Steel Sky.

%prep
%setup -q -n sky-cd -a2

install %{SOURCE1} bass-manual.pdf
mv bass.pdf bass-comics.pdf

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/games/%{name}

install sky.* $RPM_BUILD_ROOT%{_datadir}/games/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc bass*.pdf
%{_datadir}/games/%{name}
