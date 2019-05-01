Summary:	html-xml-utils - a number of simple utilities for manipulating HTML and XML files
Summary(pl.UTF-8):	html-xml-utils - kilka prostych narzędzi do obróbki plików HTML i XML
Name:		html-xml-utils
Version:	7.7
Release:	1
License:	W3C
Group:		Applications/Utilities
Source0:	https://www.w3.org/Tools/HTML-XML-utils/%{name}-%{version}.tar.gz
# Source0-md5:	8938567808754d188bf61800e569468f
URL:		https://www.w3.org/Tools/HTML-XML-utils/
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake
BuildRequires:	curl-devel >= 7.12.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML-XML-utils provides a number of simple utilities for manipulating
and converting HTML and XML files in various ways.

%description -l pl.UTF-8
HTML-XML-utils dostarczas kilka prostych narzędzi do obróbki i
konwersji plików HTML i XML na różne sposoby.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/asc2xml
%attr(755,root,root) %{_bindir}/hxaddid
%attr(755,root,root) %{_bindir}/hxcite
%attr(755,root,root) %{_bindir}/hxcite-mkbib
%attr(755,root,root) %{_bindir}/hxclean
%attr(755,root,root) %{_bindir}/hxcopy
%attr(755,root,root) %{_bindir}/hxcount
%attr(755,root,root) %{_bindir}/hxextract
%attr(755,root,root) %{_bindir}/hxincl
%attr(755,root,root) %{_bindir}/hxindex
%attr(755,root,root) %{_bindir}/hxmkbib
%attr(755,root,root) %{_bindir}/hxmultitoc
%attr(755,root,root) %{_bindir}/hxname2id
%attr(755,root,root) %{_bindir}/hxnormalize
%attr(755,root,root) %{_bindir}/hxnsxml
%attr(755,root,root) %{_bindir}/hxnum
%attr(755,root,root) %{_bindir}/hxpipe
%attr(755,root,root) %{_bindir}/hxprintlinks
%attr(755,root,root) %{_bindir}/hxprune
%attr(755,root,root) %{_bindir}/hxref
%attr(755,root,root) %{_bindir}/hxremove
%attr(755,root,root) %{_bindir}/hxselect
%attr(755,root,root) %{_bindir}/hxtabletrans
%attr(755,root,root) %{_bindir}/hxtoc
%attr(755,root,root) %{_bindir}/hxuncdata
%attr(755,root,root) %{_bindir}/hxunent
%attr(755,root,root) %{_bindir}/hxunpipe
%attr(755,root,root) %{_bindir}/hxunxmlns
%attr(755,root,root) %{_bindir}/hxwls
%attr(755,root,root) %{_bindir}/hxxmlns
%attr(755,root,root) %{_bindir}/xml2asc
%{_mandir}/man1/asc2xml.1.*
%{_mandir}/man1/hxaddid.1.*
%{_mandir}/man1/hxcite-mkbib.1.*
%{_mandir}/man1/hxcite.1.*
%{_mandir}/man1/hxclean.1.*
%{_mandir}/man1/hxcopy.1.*
%{_mandir}/man1/hxcount.1.*
%{_mandir}/man1/hxextract.1.*
%{_mandir}/man1/hxincl.1.*
%{_mandir}/man1/hxindex.1.*
%{_mandir}/man1/hxmkbib.1.*
%{_mandir}/man1/hxmultitoc.1.*
%{_mandir}/man1/hxname2id.1.*
%{_mandir}/man1/hxnormalize.1.*
%{_mandir}/man1/hxnsxml.1.*
%{_mandir}/man1/hxnum.1.*
%{_mandir}/man1/hxpipe.1.*
%{_mandir}/man1/hxprintlinks.1.*
%{_mandir}/man1/hxprune.1.*
%{_mandir}/man1/hxref.1.*
%{_mandir}/man1/hxremove.1.*
%{_mandir}/man1/hxselect.1.*
%{_mandir}/man1/hxtabletrans.1.*
%{_mandir}/man1/hxtoc.1.*
%{_mandir}/man1/hxuncdata.1.*
%{_mandir}/man1/hxunent.1.*
%{_mandir}/man1/hxunpipe.1.*
%{_mandir}/man1/hxunxmlns.1.*
%{_mandir}/man1/hxwls.1.*
%{_mandir}/man1/hxxmlns.1.*
%{_mandir}/man1/xml2asc.1.*
