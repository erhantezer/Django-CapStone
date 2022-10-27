
#! Converting a UUID to a string with str() yields something in the form '12345678-1234-1234-1234-123456789abc'. 
#! Tek istediğiniz benzersiz bir kimlikse, muhtemelen uuid1() veya uuid4()'ü aramalısınız. içeren bir UUID oluşturduğundan, uuid1() öğesinin
#! gizliliği tehlikeye atabileceğini unutmayın.bilgisayarın ağ adresi. uuid4() rastgele bir UUID oluşturur
#? UUID (universally unique identifier)
import uuid

def get_random_code(): #! fonksiyon adı verdik rastgele verebiliriz
    code = str(uuid.uuid4())[:11].replace("-","")
    return code

#! Burada evrensel benzersiz kimlik tanımlayıcı yı import ettik yani çağırdık ardından kendine ait method la
#! bu işlemi code değişkenine atıp döndürdük istenilen yerde çağırılacak vaziyete getirdik