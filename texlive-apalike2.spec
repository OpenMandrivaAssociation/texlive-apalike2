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
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3

%description
Described as a "local adaptation" of apalike.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/apalike2/apalike2.bst
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
