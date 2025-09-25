#/bin/sh

TMP=$(ps a)
bat >> /tmp/tmp.rmd
echo >> /tmp/tmp.rmd
echo "cat('\n')" >> /tmp/tmp.rmd

if echo "$TMP" | grep -q fifo_rscript; then
  Rscript --save --restore /tmp/tmp.rmd &> /tmp/fifo_rscript
  if [ -e Rplots.pdf ]; then
    zathura Rplots.pdf
    rm Rplots.pdf
  fi
fi

rm /tmp/tmp.rmd
