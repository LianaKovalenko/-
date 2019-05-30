#Дано
vid_produkzii=['Молоко 0,5%','Молоко 1,5%','Молоко 2,5%','Молоко 3,2%','Молоко 3,5%','Молоко 6,0%','Кефир 1,0%','Кефир 2,5%','Творог 4,0%','Творог 18.0%']
po_plany=[222.9,259.4,884.0,251.2,128.4,21.8,111.0,184.4,135.2,25.7]
fakticheski=[225.3,260.4,850.1,245.7,130.6,20.1,115.8,185.0,138.2,22.5]
produkzia=[0.5,1.5,2.5,3.2,3.5,6.0,1.0,2.5,4.0,18.0]
etalon=[2.5,2.5,2.5,2.5,2.5,2.5,2.5,2.5,2.5,2.5]

#Нахождение коэфф.пересчета для каждого вида продукции, если эталон 2,5%
koeffiz_perecheta=[x/y for x,y in zip(produkzia,etalon)]
list_koeffiz_perecheta=dict(zip(vid_produkzii,koeffiz_perecheta))
print('1)Если эталон = 2,5 процента, то по каждому виду продукции коэффециент пересчета равен: %s '%(list_koeffiz_perecheta))

#Найдем выпуск продукции по плану с учетом умножения на коэфф.пересчета
po_plany_uchitivaya_perechet=[x/y for x,y in zip(po_plany,koeffiz_perecheta)]
summa_po_plany_uchitivaya_perechet=sum(po_plany_uchitivaya_perechet)
list_po_plany_uchitivaya_perechet=dict(zip(vid_produkzii,po_plany_uchitivaya_perechet))
print('2)Выпуск продукции по плану, с учетом пересчета на коффициент пересчета, равен: %s '%(list_po_plany_uchitivaya_perechet))
print('3)Сумма выпуска всей продукции по плану, с учетом пересчета на коффициент пересчета, равна: %s '%(summa_po_plany_uchitivaya_perechet))

#Найдем выпуск продукции фактически с учетом умножения на коэфф.пересчета
fakticheski_uchitivaya_perechet=[x/y for x,y in zip(fakticheski,koeffiz_perecheta)]
summa_fakticheski_uchitivaya_perechet=sum(fakticheski_uchitivaya_perechet)
list_fakticheski_uchitivaya_perechet=dict(zip(vid_produkzii,fakticheski_uchitivaya_perechet))
print('4)Выпуск продукции по факту, с учетом пересчета на коффициент пересчета, равен: %s '%(list_po_plany_uchitivaya_perechet))
print('5)Сумма выпуска всей продукции по факту, с учетом пересчета на коффициент пересчета, равна: %s '%(summa_fakticheski_uchitivaya_perechet))

#Определим относительные показатели реализации плана по каждому виду продукта
pokazateli_realizacii=[(x/y)*100 for x,y in zip(fakticheski_uchitivaya_perechet,po_plany_uchitivaya_perechet)]
list_fpokazateli_realizacii=dict(zip(vid_produkzii,pokazateli_realizacii))
print('6) Относительные показатели реализации плана по каждому виду продукции равны: %s '%(list_fpokazateli_realizacii))

#Определим относительные показатели реализации плана в целом
pokazateli_realizacii_v_celom=(sum(fakticheski_uchitivaya_perechet)/sum(po_plany_uchitivaya_perechet))*100
print('7) Относительные показатели реализации плана по в целом по всем видам продукции равны: %s процентов'%(pokazateli_realizacii_v_celom))

#Найдем самый высокий и самый низкий относительный показатель реализации плана
max_pokazateli_realizacii=max(list_fpokazateli_realizacii, key=list_fpokazateli_realizacii.get)
print('8)Cамый высокий показатель реализации плана(Вид продукции;показатель в процентах):')
print(max_pokazateli_realizacii,list_fpokazateli_realizacii[max_pokazateli_realizacii])
min_pokazateli_realizacii=min(list_fpokazateli_realizacii, key=list_fpokazateli_realizacii.get)
print('9)Cамый низкий показатель реализации плана(Вид продукции;показатель в процентах):')
print(min_pokazateli_realizacii,list_fpokazateli_realizacii[min_pokazateli_realizacii])

pokazateli_realizacii_v_celom2=float(pokazateli_realizacii_v_celom)
a=100-pokazateli_realizacii_v_celom2
print('ВЫВОД:')
if pokazateli_realizacii_v_celom2>100:
       print('План реализации продукции перевыполнен на %s процент(ов)' %a)
elif pokazateli_realizacii_v_celom2==100:
       print('План реализации продукции выполнен')
elif pokazateli_realizacii_v_celom2<100:
       print('План реализации продукции не выполнен на %s процент(ов)' %a)

