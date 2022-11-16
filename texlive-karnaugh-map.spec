Name:		texlive-karnaugh-map
Version:	61614
Release:	1
Summary:	LaTeX package for drawing karnaugh maps with up to 6 variables
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/karnaugh-map
License:	cc-by-sa-3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/karnaugh-map.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/karnaugh-map.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/karnaugh-map.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package draws karnaugh maps with 2, 3, 4, 5, and 6
variables. It also contains commands for filling the karnaugh
map with terms semi-automatically or manually. Last but not
least it contains commands for drawing implicants on top of the
map. This package depends on the keyval, kvoptions, TikZ,
xparse, and xstring packages.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/karnaugh-map
%{_texmfdistdir}/tex/latex/karnaugh-map
%doc %{_texmfdistdir}/doc/latex/karnaugh-map

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
