Name:		texlive-fcavtex
Version:	38074
Release:	1
Summary:	A thesis class for the FCAV/UNESP (Brazil)
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/fcavtex
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fcavtex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fcavtex.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a class and a bibliography style for the
FCAV-UNESP (Faculdade de Ciencias Agrarias e Veterinarias de
Jaboticabal UNESP) brazilian university, written based on the
institution rules for thesis publications.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/fcavtex
%{_texmfdistdir}/bibtex/bst/fcavtex
%doc %{_texmfdistdir}/doc/latex/fcavtex

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
