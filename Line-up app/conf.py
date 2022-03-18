# Global variables
#iculp_logo_path = 'C:\\Users\\baris\\Desktop\\WIP\\Eyewitness_Identification_Project-main\\Eyewitness_Identification_Project-main\\images\\iculp.png'

# Logo Path
lineup_logo_initial = 'images\\lineup_initial.png'
lineup_logo_small = 'images\\lineup_logo.png'
lineup_logo_main = 'images\\lineup_main.png'

# Button
start_button_text = "BAŞLA"
confirmation_button_text = "Tamam"
consent_button_text = "Analize basla"
final_popup_accept = "Anladim, devam \netmek istiyorum"
final_popup_reject = "Anlamadim, devam \netmek istemiyorum"
button_file_browser_text = "Upload a picture"
button_file_remove_text = "Fotografı Kaldır"
police_submit_button_text = "Aramaya Başla"
witness_submit_button_text = "Teşhise Başla"
button_image_upload = "Foto Yükle"

# Label
program_description = "Yapay Zeka Tabanlı Teşhis Uygulaması"
version_info = "v1.0"

# Popup
police_warning_info = "Dikkat: \n Bu bölüm soruşturumada görevli polis memuru tarafından doldurulmalıdır. \n Lütfen Teşhis dizisi oluşturulana kadar geçen aşamaların \n tanık/lar tarafından görülmediğinden emin olunuz!"
image_upload_text = "You can only use \nJPEG, JPG and PNG file formats."
filler_image_upload_text = "You can only use \n JPEG, JPG and PNG file formats."
image_upload_menu_info = "Süpheli Fotografi Yükleme Arayüzü"
filler_image_upload_menu_info = "Dolgu Fotografi Yükleme Arayüzü"
popup_size = ""
suspect_image_path = ""
f1_image_path = ""
f2_image_path = ""
f3_image_path = ""
f4_image_path = ""
f5_image_path = ""
police_error_popup_text = "Lütfen tüm verileri giriniz ve süpheli resmini yükleyiniz!"
witness_error_popup_text = "Lütfen tüm verileri giriniz"
error_popup_title = "Hata"
popup_msg = ["Bir sonraki aşamada size altı farklı kişinin yer aldığı \nbir grup fotoğraf göstereceğiz. Tanık [veya mağdur]\n olduğunuz suçu işleyen kişinin fotoğrafı \nbu kişiler arasında olabilir veya olmayabilir.",
             "Bazı fiziksel farklılıklar (saç stili, sakal-bıyık, \ngözlük, şapka vb.) nedeniyle fotoğraftaki kişi gerçek \nhayattakinden farklı görünebilir. Kişilerin ten renginin\n fotoğrafta gerçek hayatta olduğundan daha açık veya \nkoyu gösterebileceğini unutmayın.",
             "Gösterilecek olan fotoğraflar belirli bir sıralamaya\nsahip olmayıp birazdan göreceğiniz fotoğrafları\n istediğiniz kadar inceleyebilirsiniz.",
             "Gösterilecek olan fotoğraflar arasında size tanıdık \ngelen biri olmayabilir. Birini seçseniz de seçmeseniz\n de olay kolluk kuvvetleri tarafından araştırılmaya \ndevam edilecektir.",
             "Size yardımcı olan memur \n gerçek şüphelinin kim olduğunu bilmemektedir.",
             "Fotoğraflarda yer alması muhtemel herhangi bir işaretin, \n sayının veya farklılığın teşhis ile bir ilgisi \nbulunmamaktadır." ]
popup_msg1 = ""
popup_msg2 = ""
popup_msg3 = "Uyari 3"
popup_msg4 = "Uyari 4"
popup_msg5 = "Uyari 5"
popup_msg6 = "Uyari 6"
popup_title = "Uyari !!!"
popup_reject = "Lütfen, polis ile konusun"
popup_wrong_password = "Password yanlis!"
witness_statement_confidence = "Seçiminizden ne kadar eminsiniz?"
lineup_warning = "Fotoğraflı teşhis dizisinin oluşturulabilmesi için \n 5 (beş) dolgu kişinin seçilmesi gerekmektedir."

# Give the parameter for the final report
dict_police_parameters = {}
list_police_parameters = ["Soruşturma Numarası: ", "Suç Tipi: ", "Olay Yeri:", "Olay Zamanı:","Şüpheli Sayısı:","Tanık Sayısı: ","Polis Memurunun Adı:","Polis Memurunun Soyadı:","PM Sicil Numarası: ","Tanık TC KN:","Tanığın Adı:","Tanığın Soyadı: ","Doğum Tarihi:","Cinsiyeti","Etnik Kökeni"]
dict_witness_parameters = {}
param_esgal_tarifi = "Esgal Tarifi"
# Her 38 harften sonra \n ile bölünmeli
list_witness_parameters = ["Soruşturma Numarası", "A. TANIK BİLGİLERİ","Tanık TCKN","Tanık Ad","Tanık Soyad","Tanık Cinsiyet","Tanık Doğum Tarihi","Nüfus Kayıt Bilgileri","İkamet Adresi","İletişim Bilgileri","B. OLAY BİLGİLERİ","Olayın mağduru musunuz?","Olaya tanık olduğunuz tarih/saat\nnedir?","Olayı doğrudan gördünüz mü?","Olayı ne kadar süre ile \ngözlemlediniz?","Faile olan uzaklığınız ne kadardı?","Gözlük veya lens kullanıyor \nmusunuz?","Evetse, olay anında kullanıyor \nmuydunuz?","Olay günü bilincinizi etkileyecek \nbir ilaç, madde veya alkol aldınız mı?","Evetse, neydi? Ne zaman ve ne\nkadar kullanmıştınız?","Fiziksel bir şiddet olayına \ntanık oldunuz mu?","Silah kullanıldı mı?","Kullanıldıysa, ne tür bir silah \nkullanıldı?","Olayda size yönelmiş bir tehdit \nveya şiddet eylemi mevcut muydu?","C. FAİL BİLGİLERİ","Faili olay öncesinde tanıyor\n muydunuz?","Şüphelinin resmini teşhis\nişleminden önce gördünüz mü?","Gördüyseniz nerede?\nAranıyor ilanı, gazete, sosyal medya vb.","Şüphelinin robot resminin \nçizilmesine yardımcı  oldunuz mu?",param_esgal_tarifi]
#list_witness_parameters = ["Tanik Adi", "Tanik TCKN",param_esgal_tarifi]
final_lineup_list = []
# Password for the police
password_police = "123456"

# Position of Entry and Label
relx_label = 0.04
rely = 0.17
relx_entry = 0.18

page1_relx_label = 0.17
page1_rely = 0.17
page1_relx_entry = 0.27

screen_height = 803
screen_width = 1203







