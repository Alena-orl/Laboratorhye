# TODO Найдите количество книг, которое можно разместить на дискете

mem_for_one_book=4*25*50*100 #bytes
mem_on_one_disk=1.44*1024*1024

print("Количество книг, помещающихся на дискету:", int(mem_on_one_disk//mem_for_one_book))
