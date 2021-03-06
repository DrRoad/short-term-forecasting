# copy all files from wiki/ to docs/
cp -a wiki/* docs/

# change directory to docs/
cd docs
    
# convert homepage to tex, which will be inserted via the template
pandoc ../wiki/Home.md --output preface.tex

# convert wiki to pdf via pdflatex
pandoc \
    --template=pandoc.tex \
    --from markdown+backtick_code_blocks \
    --metadata title="Short-term forecasting of electricity generation, demand and market prices using machine learning" \
    --metadata author="Nithiya Streethran" \
    --metadata subject="ENergy SYStems in TRAnsition (ENSYSTRA)" \
    --variable date="`date '+%-d %B %Y'`" \
    --variable keywords="forecasting, electricity market, machine learning, energy transition" \
    --metadata copyright="Copyright (c) `date '+%Y'` Nithiya Streethran. Licensed under the GNU Free Documentation License Version 1.3." \
    --metadata licenseurl="https://www.gnu.org/licenses/fdl-1.3" \
    --metadata contactemail="nmstreethran@gmail.com" \
    --variable fontsize=10pt \
    --variable geometry:margin=2.5cm \
    --variable papersize="a4" \
    --variable fontfamily="mathpazo" \
    --variable classoption="twoside" \
    --variable linkcolor=blue \
    --variable toccolor=blue \
    --variable urlcolor=blue \
    --toc \
    --variable toc-title="Table of Contents" \
    --variable lof=true \
    --variable lot=true \
    --filter pandoc-crossref \
    --metadata autoSectionLabels=true \
    --bibliography References.bib \
    --filter pandoc-citeproc \
    --csl IEEEurl.csl \
    --metadata link-citations=true \
    --reference-location=block \
    --listings \
    ../wiki/Background.md \
    ../wiki/Problem-definition.md \
    ../wiki/Objectives.md \
    ../wiki/Regions.md \
    ../wiki/Data.md \
    ../wiki/Methodology.md \
    ../wiki/Abbreviations.md \
    refs.md \
    ../wiki/License.md \
    --output docs.pdf

# convert wiki to html
pandoc --standalone \
    --from markdown+backtick_code_blocks \
    --highlight-style=tango \
    --metadata title="Short-term forecasting of electricity generation, demand and market prices using machine learning" \
    --metadata author="Nithiya Streethran" \
    --metadata date="`date '+%-d %B %Y'`" \
    --toc \
    --toc-depth=3 \
    --css solarized.css \
    --filter pandoc-crossref \
    --metadata autoSectionLabels=true \
    --bibliography References.bib \
    --filter pandoc-citeproc \
    --csl IEEEurl.csl \
    --metadata link-citations=true \
    ../wiki/Home.md \
    logos.html \
    ../wiki/Background.md \
    ../wiki/Problem-definition.md \
    ../wiki/Objectives.md \
    ../wiki/Regions.md \
    ../wiki/Data.md \
    ../wiki/Methodology.md \
    ../wiki/Abbreviations.md \
    refs.md \
    ../wiki/License.md \
    --output index.html

# change directory back to the previous level
cd ..
