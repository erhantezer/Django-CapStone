#### CharField 255 karaktere kadar stringler için kullanılan alan tipidir. max_length argümanı tanımlanması zorunludur. max_length argümanı alanın alabileceği maksimum karakter sayısını belirler. Ürünümüz için isim alanı ekleylim. En fazla 200 karakter alabilsin.
<hr>
 <div style="color: red;">1. verbose_name :</div> alanın admin sayfasıi form gibi çıktılarda görüntülecek adıdır. Eğer girilmezse değişken kullanılır.
<hr>
<div style="color: red;">2. default : </div> argümanına girilen değer eğer alanın değeri boş ise veritabanına eklenecek olan varsayılan değerdir.
<hr>
<div style="color: red;">3. blank:</div> argümanının veritabanı alanı ile herhangi bir ilgisi yoktur. Form validasyonu için kullanılır. Eğer True ise forma boş değer girilmesi izin verir. Aksi taktirde değer girmeye zorlar.
<hr>
<div style="color: red;">4. null: </div> argümanı eğer True ise bu alan veritabanında boş değer alabilir. Aksi taktirde alana bir değer girilmesini zorunlu tutar.
<hr>
<div style="color: red;">5. unique: </div> argümanı eğer True ise alanın benzersiz olduğunu belirtir. O alan aynı değeri sadece bir kez alabilir.
<hr>
<div style="color: red;">6. editable: </div> argümanı eğer False seçilirse ilgili alan admin paneli ve formlarda görüntülenmez. Varsayılan değeri True’dur.
<hr>
<div style="color: red;">7. db_index: </div> argümanı index oluşturulması istenilen alanlar için True seçilir.
<hr>
<div style="color: red;">8. db_column: </div> argümanı ilgili alanın veritabanında kullanılacak ismini ayarlar. Eğer girilmez ise alan adi kullanılır. Hatırlarsanız
<hr>
<div style="color: red;">9. help_text: </div> argümanı alanın formlarda görüntülecek olan ilave yardım metnidir.
<hr>

### <div style="color: blue;">SlugField, Slug oluşturmak için kullanılan alan tipidir. harf, sayı, alt çizgi ve kısa çizgi alabilir. Genellikle url için kullanılır. max_length argümanı alır. max_length default 50 olarak ayarlanmıştır. db_index argümanı default olarak True ayarlanmıştır.</div>
