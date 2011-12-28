# revision 15878
# category Package
# catalog-ctan /biblio/bibtex/contrib/apalike2/apalike2.bst
# catalog-date 2009-11-09 13:03:38 +0100
# catalog-license other-free
# catalog-version undef
Name:		texlive-apalike2
Version:	20091109
Release:	1
Summary:	Bibliography style that approaches APA requirements
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/biblio/bibtex/contrib/apalike2/apalike2.bst
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/apalike2.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Described as a "local adaptation" of apalike.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/apalike2/apalike2.bst

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex %{buildroot}%{_texmfdistdir}
