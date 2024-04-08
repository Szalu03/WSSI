<details>
<summary>ZAD1.1</summary>
 <ul>
<p> A) X jest rodzeństwem Y</p>
<p> B) X jest kuzynem Y</p>
<p> C) wnuk/wnuczka</p>
<p> D) y jest ojczymem dla x</p>
<p> E) rodzeństwo przyrodnie</p>
<p> F) szwagier/szwagierka</p>
<p> G) rodzeństwo przyrodnie</p>
 </ul>


</details>
<details><summary>ZAD1.2</summary>
<ul><p> A) rodzeństwo:
 <ul>
   <p>relacjarodzenstwo(X,Y) :-</p>
  <p>rodzic(X,Z),</p>
 <p> rodzic(X,H),</p>
  <p>rodzic(Y,H),</p>
 <p> rodzic(Y,Z),</p>
 <p> X\=Y. </ul></p>
</p>
<p> B) kuzynostwo:
 <ul>
   <p>kuzyn(X,Y) :-</p>
 <p> rodzic(X,Z),</p>
 <p> rodzic(Z,H),</p>
 <p> rodzic(Y,D),</p>
<p>  rodzic(D,H).</ul></p>
</p>
<p> C) wnuk/wnuczka:
 <ul>
  <p>wnuk/wnuczka(X,Y) :-</p>
 <p>  rodzic(H,B),</p>
  <p> rodzic(H,C),</p>
 <p>  rodzic(B,X),</p>
 <p>  rodzic(C,Y).</ul></p>
</p>
<p> D) ojczym:
 <ul>
 <p> ojczym(X,Y) :-</p>
 <p> rodzic(X,D),</p>
 <p> rodzic(H,D),</p>
 <p> rodzic(H,Y).</ul></p>
</p>
<p> E) ojczym:
 <ul>
   <p>przyrodnierodzenstwo(X,Y) :-</p>
 <p> rodzic(X,H),</p>
 <p> rodzic(X,I),</p>
  <p>rodzic(Y,I),</p>
 <p> rodzic(Y,J).</ul></p>
</p>
<p> F) szwagier/szwagierka:
 <ul>
   <p>szwagier(X,Y) :-</p>
  <p>rodzic(H,X),</p>
<p>  rodzic(H,B),</p>
 <p> rodzic(B,J),</p>
<p>  rodzic(Y,J).</ul></p>
</p>
 <p> G) przyrodnie rodzenstwo:
 <ul>
   <p>przyrodnierodzenstwo(X,Y) :-</p>
 <p> rodzic(Y,H),</p>
  <p>rodzic(Y,I),</p>
 <p> rodzic(X,I),</p>
 <p> rodzic(X,J),</p>
<p> rodzic(H,J).</ul></p>
</p>
</ul>
</details>
<details><summary>ZAD2</summary>
 <ul>
 <p>kobieta(X) :-</p><ul>
   <p>  \+mezczyzna(X).</p> </ul>

 <p>ojciec(X,Y) :-</p><ul>
    <p> rodzic(Y,X),</p>
    <p> mezczyzna(X).</p> </ul>

 <p>matka(X,Y) :-</p><ul>
     <p>rodzic(Y,X),</p>
    <p> kobieta(X).</p> </ul>

 <p>corka(X,Y) :-</p><ul>
    <p> rodzic(X,Y),</p>
    <p> kobieta(X).</p> </ul>

 <p>brat_rodzony(X,Y) :-</p><ul>
    <p> rodzic(X,H),</p>
   <p>  rodzic(X,J),</p>
    <p> rodzic(Y,H),</p>
   <p>  rodzic(Y,J),</p>
   <p>  mezczyzna(X).</p> </ul>

 <p>brat_przyrodni(X,Y) :-</p><ul>
     <p>rodzic(X,H),</p>
     <p>rodzic(X,J),</p>
  <p>   rodzic(Y,H),</p>
  <p>   rodzic(Y,I),</p>
   <p>  mezczyzna(X).</p> </ul>

 <p>kuzyn(X,Y) :-</p><ul>
     <p>rodzic(X,H),</p>
   <p>  rodzic(H,J),</p>
    <p> rodzic(Y,I),</p>
    <p> rodzic(I,J).</p> </ul>

 <p>dziadek_od_strony_ojca(X,Y) :-</p><ul>
    <p> ojciec(H,Y),</p>
    <p> ojciec(X,H).</p> </ul>

 <p>dziadek_od_strony_matki(X,Y) :-</p><ul>
 <p>matka(H,Y),</p>
   <p>  ojciec(Y,H).</p> </ul>

 <p>dziadek(X,Y) :-</p><ul>
    <p> rodzic(Y,H),</p>
   <p>  ojciec(X,H).</p> </ul>

 <p>babcia(X,Y) :-</p><ul>
 <p>    rodzic(Y,H),</p>
     <p>matka(X,H).</p> </ul>

 <p>wnuczka(X,Y) :-</p><ul>
     <p>rodzic(Y,H),</p>
   <p>  rodzic(H,X),</p>
   <p>  kobieta(Y).</p> </ul>
   
 <p>przodek_do2pokolenia_wstecz(X,Y) :-</p>
    <p> rodzic(Y,H),</p>
     <p>rodzic(H,X).</p> </ul>

<p>przodek_do3pokolenia_wstecz(X,Y) :-</p>
<ul>
  <p>  rodzic(Y,H),</p>
   <p> rodzic(J,H),</p>
  <p>  rodzic(H,X).</p></ul>
 </ul>
