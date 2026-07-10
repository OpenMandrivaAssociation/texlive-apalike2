%global tl_name apalike2
%global tl_revision 76790

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Bibliography style that approaches APA requirements
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/biblio/bibtex/contrib/apalike2
License:	knuth
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/apalike2.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Described as a "local adaptation" of apalike (which is part of the base
BibTeX distribution).

%prep
%setup -q -c
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/bibtex
%dir %{_datadir}/texmf-dist/bibtex/bst
%dir %{_datadir}/texmf-dist/bibtex/bst/apalike2
%{_datadir}/texmf-dist/bibtex/bst/apalike2/apalike2.bst
