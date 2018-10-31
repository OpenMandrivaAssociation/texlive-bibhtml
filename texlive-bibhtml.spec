# revision 31607
# category Package
# catalog-ctan /biblio/bibtex/contrib/bibhtml
# catalog-date 2013-09-08 21:40:59 +0200
# catalog-license gpl
# catalog-version 2.0.2
Name:		texlive-bibhtml
Version:	2.0.2
Release:	10
Summary:	BibTeX support for HTML files
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/biblio/bibtex/contrib/bibhtml
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bibhtml.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bibhtml.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Bibhtml consists of a Perl script and a set of BibTeX style
files, which together allow you to output a bibliography as a
collection of HTML files. The references in the text are linked
directly to the corresponding bibliography entry, and if a URL
is defined in the entry within the BibTeX database file, then
the generated bibliography entry is linked to this. The package
provides three different style files derived from each of the
standard plain.bst and alpha.bst, as well as two style files
derived from abbrv.bst and unsrt.bst (i.e., eight in total).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/bibhtml/abbrvhtml.bst
%{_texmfdistdir}/bibtex/bst/bibhtml/alphahtml.bst
%{_texmfdistdir}/bibtex/bst/bibhtml/alphahtmldate.bst
%{_texmfdistdir}/bibtex/bst/bibhtml/alphahtmldater.bst
%{_texmfdistdir}/bibtex/bst/bibhtml/plainhtml.bst
%{_texmfdistdir}/bibtex/bst/bibhtml/plainhtmldate.bst
%{_texmfdistdir}/bibtex/bst/bibhtml/plainhtmldater.bst
%{_texmfdistdir}/bibtex/bst/bibhtml/unsrthtml.bst
%doc %{_texmfdistdir}/doc/bibtex/bibhtml/LICENCE
%doc %{_texmfdistdir}/doc/bibtex/bibhtml/README
%doc %{_texmfdistdir}/doc/bibtex/bibhtml/bibhtml
%doc %{_texmfdistdir}/doc/bibtex/bibhtml/bibhtml-extract-aux.xslt
%doc %{_texmfdistdir}/doc/bibtex/bibhtml/bibhtml-insert-bib.xslt
%doc %{_texmfdistdir}/doc/bibtex/bibhtml/bibhtml.html
%doc %{_texmfdistdir}/doc/bibtex/bibhtml/bibrefs.bib
%doc %{_texmfdistdir}/doc/bibtex/bibhtml/detex.sed
%doc %{_texmfdistdir}/doc/bibtex/bibhtml/style.css

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex doc %{buildroot}%{_texmfdistdir}
