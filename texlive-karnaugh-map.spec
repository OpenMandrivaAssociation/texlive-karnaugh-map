%global tl_name karnaugh-map
%global tl_revision 61614

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.0
Release:	%{tl_revision}.1
Summary:	LaTeX package for drawing karnaugh maps with up to 6 variables
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/karnaugh-map
License:	cc-by-sa-3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/karnaugh-map.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/karnaugh-map.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/karnaugh-map.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package draws karnaugh maps with 2, 3, 4, 5, and 6 variables. It
also contains commands for filling the karnaugh map with terms semi-
automatically or manually. Last but not least it contains commands for
drawing implicants on top of the map. This package depends on the
keyval, kvoptions, TikZ, xparse, and xstring packages.

