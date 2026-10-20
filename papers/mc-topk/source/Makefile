TEX := main
ARXIV_TARBALL := arxiv-monte-carlo-topk.tar.gz

.PHONY: pdf arxiv clean distclean

pdf:
	latexmk -pdf -interaction=nonstopmode -halt-on-error $(TEX).tex

arxiv: pdf
	test -f $(TEX).bbl
	rm -f $(ARXIV_TARBALL)
	tar -czf $(ARXIV_TARBALL) --exclude='figures/README.md' \
		$(TEX).tex arxiv.sty $(TEX).bbl references.bib sections figures

clean:
	latexmk -c

distclean:
	latexmk -C
	rm -f $(ARXIV_TARBALL)
