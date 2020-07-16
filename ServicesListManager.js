// Класс для управления услугами
class ServicesListManager {
    // Список услуг
    list = [];

    // Добавляет услугу
    add(service = {}) {  
        // Собираем новую услугу      
        let newService = { 
            id: this.list.length == 0 
                ? 0 
                : this.list[this.list.length-1].id + 1,
            name: service.name || 'Новая услуга', 
            time: service.time || new Date().toISOString() 
        };

        // Добавляем услугу в список
        this.list = [...this.list, newService];
    }

    // Обновляет услугу
    update(service) {
        if (service == null) {
            console.error('service должен быть объектом');
            return;
        }

        if (this.list.find((item) => item.id == service.id) == null) {
            console.error('Нет услуги с указанным id');
            return;
        }

        // Обновляем услугу в списке услуг
        this.list = this.list.map(item => {
            if (item.id == service.id) {
                return service;
            }
            return item;
        })

    }

    // Удаляет услугу
    delete(id) {
        if (this.list.find((item) => item.id == id) == null) {
            console.error('Нет услуги с указанным id');
            return;
        }

        // Удаляем элемент из массива
        this.list = this.list.filter(item => item.id != id);
    }
}

const services = new ServicesListManager();

// Пример использования
services.add();
services.add({ name: 'Услуга 1' });
services.add({ name: 'Услуга 2', time: '2020-01-22T17:30' });
services.update({ id: 2, name: 'Услуга 2', time: '2020-01-24T18:30' });
console.log(services.list);

services.delete(0);
console.log(services.list);
