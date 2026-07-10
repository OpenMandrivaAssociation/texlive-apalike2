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
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Described as a "local adaptation" of apalike (which is part of the base
BibTeX distribution).

