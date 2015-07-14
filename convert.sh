cat input.dat | sed 's/</\\lt /g' \
    | sed 's/>/\\gt /g' \
    | sed '/^\s*$/d' \
    | sed '/%.*$/d' \
    | sed 's/\\begin{frame}\[\?.*\]\?/<section>/g' \
    | sed 's/\\end{frame}/<\/section>/g' \
    | sed 's/\\frametitle{\(.*\)}/<h2>\1<\/h2>/g' \
    | sed '/\\section{.*}.*$/d' \
    | awk 'BEGIN{p=1;content=""} /\\item/ { if (p==1) {p=0} else {print "<li>"content"</li>"; content="";}} /\\end\{itemize\}/ { if (p==0) {print "<li>"content"</li>"; content=""; p=1;} } {if (p==1) {print} else {content=content$0"\n";}}' \
    | sed 's/\\begin{itemize}/<ul>/g' \
    | sed 's/\\end{itemize}/<\/ul>/g' \
    | sed 's/\\item//g' \
    | sed 's/\\bm/\\boldsymbol/g' \
    | sed 's/\\includegraphics\[\?.*\]\?{\(.*\)}/<img src="\1"><\/img>/g' \
    | sed 's/\\begin{center}//g' \
    | sed 's/\\end{center}//g' \
    | sed 's/\\begin{flushleft}/<div style="text-align:left;">/g' \
    | sed 's/\\end{flushleft}/<\/div>/g' \
    | sed 's/``/&ldquo;/g' \
    | sed 's/''/&rdquo;/g' \
    | sed 's/\\end{center}//g' \
	  > output.dat

