%global tl_name bibhtml
%global tl_revision 31607

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.0.2
Release:	%{tl_revision}.1
Summary:	BibTeX support for HTML files
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/biblio/bibtex/contrib/bibhtml
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bibhtml.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bibhtml.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Bibhtml consists of a Perl script and a set of BibTeX style files, which
together allow you to output a bibliography as a collection of HTML
files. The references in the text are linked directly to the
corresponding bibliography entry, and if a URL is defined in the entry
within the BibTeX database file, then the generated bibliography entry
is linked to this. The package provides three different style files
derived from each of the standard plain.bst and alpha.bst, as well as
two style files derived from abbrv.bst and unsrt.bst (i.e., eight in
total).

