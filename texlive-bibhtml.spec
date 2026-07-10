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
Requires(pre):	texlive-tlpkg
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

%prep
%setup -q -c -a1
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
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/bibtex/bst
%dir %{_datadir}/texmf-dist/doc/bibtex
%dir %{_datadir}/texmf-dist/bibtex/bst/bibhtml
%dir %{_datadir}/texmf-dist/doc/bibtex/bibhtml
%{_datadir}/texmf-dist/bibtex/bst/bibhtml/abbrvhtml.bst
%{_datadir}/texmf-dist/bibtex/bst/bibhtml/alphahtml.bst
%{_datadir}/texmf-dist/bibtex/bst/bibhtml/alphahtmldate.bst
%{_datadir}/texmf-dist/bibtex/bst/bibhtml/alphahtmldater.bst
%{_datadir}/texmf-dist/bibtex/bst/bibhtml/plainhtml.bst
%{_datadir}/texmf-dist/bibtex/bst/bibhtml/plainhtmldate.bst
%{_datadir}/texmf-dist/bibtex/bst/bibhtml/plainhtmldater.bst
%{_datadir}/texmf-dist/bibtex/bst/bibhtml/unsrthtml.bst
%doc %{_datadir}/texmf-dist/doc/bibtex/bibhtml/LICENCE
%doc %{_datadir}/texmf-dist/doc/bibtex/bibhtml/README
%doc %{_datadir}/texmf-dist/doc/bibtex/bibhtml/bibhtml
%doc %{_datadir}/texmf-dist/doc/bibtex/bibhtml/bibhtml-extract-aux.xslt
%doc %{_datadir}/texmf-dist/doc/bibtex/bibhtml/bibhtml-insert-bib.xslt
%doc %{_datadir}/texmf-dist/doc/bibtex/bibhtml/bibhtml.html
%doc %{_datadir}/texmf-dist/doc/bibtex/bibhtml/bibrefs.bib
%doc %{_datadir}/texmf-dist/doc/bibtex/bibhtml/detex.sed
%doc %{_datadir}/texmf-dist/doc/bibtex/bibhtml/style.css
