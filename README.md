# ONS_StorytellingData

## View all doumentation at https://wolfiex.github.io/ONS_StorytellingData/storytelling.html



```
all:
	@echo 'Welcome to the Makefile'

install:
	pip install openpyxl pandas tqdm pdoc

sillyformat: $(DATADIR)/xlsx/*.xlsx
	mkdir -p $(DATADIR)/fixedformatting;
	for file in $^ ; do \
		echo 'starting ' $${file} ; \
		$(PYTHON) -m excel2csv $${file} -o $(DATADIR)/fixedformatting; \
	done

story:
	python -m storytelling

document:
	pdoc --output-dir docs --logo https://cdn.ons.gov.uk/assets/images/ons-logo/v2/ons-logo.svg --show-source storytelling



```