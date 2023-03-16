const trumpIdEl = document.querySelector('.trump-id'),
    addFormOverlay = document.querySelector('.sheme__map-overlay'), // Елеиент формы загрузки файла ВТД
    sliderRow = document.querySelector('.slider__row'), // Контейнер для слайдов
    searchTrumpInput = document.querySelector('.search-trump'),// Инпут для поиска трубы
    nextSlideBtn = document.querySelector('.trump-nav__next'),
    prevSlideBtn = document.querySelector('.trump-nav__prev');

let trumpId = trumpIdEl.innerHTML, // Id участка в шаблоне
    searchTrumpInputVal = '', // Значение инпута для поиска
    arrayIndex = 0, // Номер массива для рендера
    arrayLength;


// Функция получения ресурсов
const getResource = async (url, varr) => {
    const res = await fetch(url);

    if (!res.ok) {
        throw new Error(`Ошибка запроса ${url}, Статус: ${res.status}`);
    }

    return await res.json();
}

let trumpsArr = [];
// Получение труб из базы и запись в массив trumpsArr
getResource("../../getTrump")
    .then(data => {

        let subarray = []; // Массив с массивами по 15 объектов.
        let trumpsArr = [];
        let tehnicUch = [];


        data.truba.forEach(objTruba => {
            if (objTruba.uch_trub_id == +trumpId) {
                trumpsArr.push(objTruba);
            }
        });
        // Если трубы в массиве есть показать их, игаче вывести кнопку загрузки.
        if (trumpsArr.length != 0) {
            // Add Elements Map
            removeHideElementsMap();

            // Добавление объектов с техникой в массив трубы
            addTehnic(trumpsArr, tehnicUch);

            // Дробим основной массив на подмасивы по 15 труб
            createSubArr(trumpsArr, subarray);

            setTimeout(() => {

                appendTrumps(subarray, arrayIndex);
                clickTrump(trumpsArr, tehnicUch);

            }, 2000);

            getResourceIntereval();

        } else {
            // Remove Elements Map
            addHideElementsMap()
        }
        // Рендер по клику на кнопки
        clickRender(subarray);
        // Рендер по клику на кнопки
        search(subarray);
    })

function getResourceIntereval() {
    setInterval(() => {
        // Получение труб из базы и запись в массив trumpsArr
        getResource("../../getTrump")
            .then(data => {

                let subarray = []; // Массив с массивами по 15 объектов.

                let trumpsArr = [];
                data.truba.forEach(objTruba => {
                    if (objTruba.uch_trub_id == +trumpId) {
                        trumpsArr.push(objTruba);
                    }
                });
                // Если трубы в массиве есть показать их, игаче вывести кнопку загрузки.
                if (trumpsArr.length != 0) {
                    // Add Elements Map
                    removeHideElementsMap()

                    // Добавление объектов с техникой в массив трубы
                    addTehnic(trumpsArr);

                    // Дробим основной массив на подмасивы по 15 труб
                    createSubArr(trumpsArr, subarray)

                    // Вставляем 15 труб с индексом 0
                    setTimeout(() => {
                        appendTrumps(subarray, arrayIndex);
                        clickTrump(trumpsArr);
                    }, 2000);

                } else {
                    // Remove Elements Map
                    addHideElementsMap()
                }
            })
    }, 2000000);

}

// Interval

//--------

// Добавление объектов с техникой в массив трубы
function addTehnic(array, tehnicUch) {

    //Получение и запись  в масив всех труб принадлежащих к участку
    getResource("../../getTehnika")
        .then(data => {
            let tehnika = [];
            data.tehnika.forEach(tehnikaObj => {
                tehnika.push(tehnikaObj);

                if (tehnikaObj.location1 == +trumpId) {
                    tehnicUch.push(tehnikaObj)
                }
            });

            array.forEach(obj => {
                tehnika.forEach(tehnikaObj => {
                    if (tehnikaObj.location2 == obj.id) {
                        let trumpTehnic = [];
                        trumpTehnic.push(tehnikaObj);
                        trumpTehnic.forEach((tehnicObj, tehnicIndex) => {
                            let tehnicIcon = `tehnic${tehnicIndex + 1}_icon`,
                                tehnicType = `tehnic${tehnicIndex + 1}_type`;
                            obj[tehnicIcon] = tehnicObj.icon;
                            obj[tehnicType] = tehnicObj.type;

                        });
                    }
                });
            });

        });
}

// Дробим основной массив на подмасивы по 15 труб
function createSubArr(array, subarray) {
    let size = 15;
    // Дробим массив на массивы длиной в 15 Записей
    for (let i = 0; i < Math.ceil(array.length / size); i++) {
        subarray[i] = array.slice((i * size), (i * size) + size);
    }

}

// Функция перебора труб и их рендеринга
function renderOneTrump(obj, item) {
    const trumpElement = document.createElement('a');
    trumpElement.classList.add('trump-wrap', `stat${obj.stage_works_id}`);
    // trumpElement.href = `/remonti/urengoi-griazovetsk-525-0-537-0/${obj.id}`
    trumpElement.innerHTML = `
    <div class="trump">

        <!-- Северная заглушка -->
        <div class="plug plug-sever" data-trump-el="${obj.zaglushka_sever}"></div>

        <!-- Перемычка север/верх -->
        <div class="jumper jumper-top" data-trump-el="${obj.peremichka_up}">
            <div class="crane-wrap">
                <div class="crane">
                    <div class="crane__left"></div>
                    <div class="crane__right"></div>
                </div>
            </div>
            <div class="vertical stat1"></div>
        </div>

        <!-- Перемычка низ -->
        <div class="jumper jumper-bottom" data-trump-el="${obj.peremichka_down}">
            <div class="vertical stat1"></div>
            <div class="crane-wrap">
                <div class="crane">
                    <div class="crane__left"></div>
                    <div class="crane__right"></div>
                </div>
            </div>
        </div>

        <!-- Отводы -->
        <div class="otvod">
            <div class="otvod__line" data-trump-el="${obj.otvod}">
                <div class="line">
                    <div></div>
                    <div></div>
                </div>
                <span class="deg" data-val>${obj.otvod_izgib}</span>
                <span class="nap" data-val>${obj.otvod_napravleniye}</span>
            </div>
        </div>

        <!-- Труба -->
        <div class="horizontal">

            <!-- Блок с коментами-дефектами -->
            <div class="text-block">
                <!-- Блок с коментами в цикле-->
                <div class="text-item comment">
                    <span class="comment-text">${obj.comment_1}</span>
                </div>
                <div class="text-item comment">
                    <span class="comment-text">${obj.comment_2}</span>
                </div>
                <div class="text-item comment">
                    <span class="comment-text">${obj.comment_3}</span>
                </div>

                <!-- Блок с дефектами в цикле-->
                <div class="text-item defect">
                    <span class="desc">
                        <span class="defect-name">${obj.def_1}</span>
                        <span class="defect-val" data-val>${obj.def_1_percent} %</span>
                        <small class="defect-km" data-val>${obj.def_1_km} км</small>
                    </span>
                </div>
                <div class="text-item defect">
                    <span class="desc">
                        <span class="defect-name">${obj.def_2}</span>
                        <span class="defect-val" data-val>${obj.def_2_percent} %</span>
                        <small class="defect-km" data-val>${obj.def_2_km} км</small>
                    </span>
                </div>
            </div>

            <!-- Номер трубы -->
            <span class="number">${obj.number}</span>

            <!-- Блок с техникой в цикле-->

            <!-- Блок с техникой -->
            <div class="tehnic-block">
                <!-- Блок с техникой в цикле-->
                <div class="text-item tehnic">
                    <img src="/static/lk/images/dist/tehnic/${obj.tehnic1_icon}" alt="${obj.tehnic1_icon}" class="icon">
                    <span class="tehnic-type">${obj.tehnic1_type}</span>
                </div>
                <div class="text-item tehnic">
                    <img src="/static/lk/images/dist/tehnic/${obj.tehnic2_icon}" alt="${obj.tehnic2_icon}" class="icon">
                    <span class="tehnic-type">${obj.tehnic2_type}</span>
                </div>
                <div class="text-item tehnic">
                    <img src="/static/lk/images/dist/tehnic/${obj.tehnic3_icon}" alt="${obj.tehnic3_icon}" class="icon">
                    <span class="tehnic-type">${obj.tehnic3_type}</span>
                </div>
            </div>

            

        </div>
        
        <!-- Южная заглушка -->
        <div class="plug plug-ug" data-trump-el="${obj.zaglushka_ug}"></div>
    </div>
    `;
    item.append(trumpElement);

    // Показываем или скрываем заглушки, перемычки, отводы
    let dataAtrs = trumpElement.querySelectorAll('[data-trump-el]');
    dataAtrs.forEach(dataAtr => {
        if (dataAtr.getAttribute('data-trump-el') === 'false') {
            dataAtr.classList.add('hide')
        } else {
            dataAtr.classList.remove('hide')
        }
    })

    // Показываем или  скрываем коменты
    let comments = trumpElement.querySelectorAll('.comment-text');
    comments.forEach(comment => {
        if (comment.innerHTML == '' || comment.innerHTML == 'null') {
            comment.parentElement.classList.add('hide');
        } else {
            comment.parentElement.classList.remove('hide');
        }
    });

    // Показываем или  скрываем дефекты
    let defects = trumpElement.querySelectorAll('.defect-name');
    defects.forEach(defect => {
        if (defect.innerHTML === '' || defect.innerHTML === 'null') {
            defect.parentElement.parentElement.classList.add('hide');
        } else {
            defect.parentElement.parentElement.classList.remove('hide');
        }
    });

    // Показываем или  скрываем технику
    let tehnics = trumpElement.querySelectorAll('.tehnic-type');
    tehnics.forEach(tehnic => {
        if (tehnic.innerHTML === '' || tehnic.innerHTML === 'undefined') {
            tehnic.parentElement.classList.add('hide');
        } else {
            tehnic.parentElement.classList.remove('hide');
        }
    });
}
function trumpsRender(array, item) {
    array.forEach(obj => {
        renderOneTrump(obj, item)
    })
}

// Функция рендеринга труб передаем subarray + arrayIndex
function appendTrumps(array, index) {
    sliderRow.innerHTML = ''
    const sliderItem = document.createElement('div');
    sliderItem.classList.add('slider__item', 'active-slide');
    trumpsRender(array[index], sliderItem);
    sliderRow.append(sliderItem);

    let sliderItemWidth = document.querySelector('.slider__item').clientWidth;
    sliderItem.style.width = `${sliderItemWidth}px`;

};

// Функция рендера по поиску
function search(subarray) {
    searchTrumpInput.addEventListener('change', e => {

        searchTrumpInputVal = searchTrumpInput.value;


        if (searchTrumpInputVal != '') {
            subarray.forEach((arr, index) => {
                arr.forEach(obj => {
                    if (searchTrumpInputVal == obj.number) {
                        arrayIndex = index;
                        appendTrumps(subarray, arrayIndex)
                        document.querySelectorAll('.trump-wrap .horizontal .number').forEach(trump => {
                            if (trump.innerHTML === searchTrumpInputVal) {
                                trump.parentElement.classList.add('horizontal_pulse')
                            }
                        })

                    }
                })
            });
        }


        let searchTrumpSpan = document.querySelector('.search-trump-span');// Message Err
        if (searchTrumpInputVal != '') {

            let arrNumbTrump = []

            for (let i = 0; i < subarray.length;) {
                subarray[i].forEach(obj => {
                    arrNumbTrump.push(obj.number);
                });
                i++;
            }
            // Ищем совпадения в масиве arrNumbTrump
            if (arrNumbTrump.includes(+searchTrumpInputVal)) {
                searchTrumpSpan.innerHTML = 'Введите № трубы и нажмите Enter';
                searchTrumpInput.style.borderColor = '';
                searchTrumpSpan.classList.remove('search-trump-span_err');
            } else {
                searchTrumpInput.style.borderColor = 'red';
                searchTrumpSpan.classList.add('search-trump-span_err');
                searchTrumpSpan.innerText = `Труба №${searchTrumpInputVal} отсутствует в базе`;
            }

        } else {
            searchTrumpInput.style.borderColor = '';
            searchTrumpSpan.innerText = `Введите № трубы и нажмите Enter`
            searchTrumpSpan.classList.remove('search-trump-span_err');
        }
    })
}

// Функция рендера по клику на кнопки
function clickRender(subarray) {
    // Удалаяем кнопки слайдера если длина массива со слайдами равна 1
    if (arrayLength == 1) {
        nextSlideBtn.classList.add('hide');
        prevSlideBtn.classList.add('hide');
    }
    // Навигация по слайдам
    nextSlideBtn.addEventListener('click', e => {
        e.preventDefault();
        if (arrayIndex < subarray.length - 1) {
            arrayIndex++;
            appendTrumps(subarray, arrayIndex);
        }
    })
    prevSlideBtn.addEventListener('click', e => {
        e.preventDefault();
        if (arrayIndex != 0) {
            arrayIndex--;
            appendTrumps(subarray, arrayIndex);
        }
    })
}

//Показ кнопки загрузки формы и скрытие вспомогательных элементов схемы
function addHideElementsMap() {
    sliderRow.innerHTML = '';
    addFormOverlay.classList.remove('hide');
    document.querySelector('.sheme__top').classList.add('hide');
    document.querySelector('.sheme__bottom').classList.add('hide');
    document.querySelector('.crane-start').classList.add('hide');
    document.querySelector('.crane-end').classList.add('hide');
}

//Показ вспомогательных элементов схемы и скрытие кнопки загрузки формы
function removeHideElementsMap() {
    addFormOverlay.classList.add('hide');
    document.querySelector('.sheme__top').classList.remove('hide');
    document.querySelector('.sheme__bottom').classList.remove('hide');
    document.querySelector('.crane-start').classList.remove('hide');
    document.querySelector('.crane-end').classList.remove('hide');
}

// РАБОТА С ФОРМОЙ ТРУБЫ
const tabsHeaderItems = document.querySelectorAll('.tabs-header__item'),
    tabsContentItems = document.querySelectorAll('.tabs-content'),
    tabslength = tabsHeaderItems.length - 1;

function clickTrump(array, tehnic) {
    document.addEventListener('click', e => {
        let trumpNumber;
        if (e.target.closest('.trump-wrap')) {
            trumpNumber = +e.target.closest('.trump-wrap').querySelector('.number').innerHTML; // Получаем номер трубы
            activeTab();
            createObjTrump()
        } else if (e.target.closest('.radio')) {
            if (e.target.closest('.radio').querySelector('.radio__box_trump-number_number')) {
                trumpNumber = +e.target.closest('.radio').querySelector('.radio__box_trump-number_number').innerHTML; // Получаем номер трубы
                activeTab();
                createObjTrump()
            }

        } else if (e.target.closest('.close_trump')) {
            tabsHeaderItems[0].classList.add('tabs-header__item_active');
            tabsHeaderItems[tabslength].classList.remove('tabs-header__item_active');
            tabsHeaderItems[tabslength].classList.add('hide');
            tabsContentItems[tabslength].classList.remove('show-tabs');
            tabsContentItems[tabslength].classList.add('hide-tabs');
            tabsContentItems[0].classList.add('show-tabs');
        }
        function activeTab() {
            // Активируем таб с трубой
            tabsContentItems.forEach(item => {
                item.classList.add('hide-tabs');
                item.classList.remove('show-tabs');
            })
            tabsHeaderItems.forEach(item => {
                item.classList.remove('tabs-header__item_active');
            })
            tabsHeaderItems[tabslength].innerHTML = `№ ${trumpNumber} <a href="#" class="close close_trump"></a>`;
            tabsHeaderItems[tabslength].classList.remove('hide');
            tabsHeaderItems[tabslength].classList.add('tabs-header__item_active');
            tabsContentItems[tabslength].classList.add('show-tabs');
        }



        function createObjTrump() {// Cоздаём обЪект с трубой
            let newArr = [],
                arrIndex;

            array.forEach((trumpsObj, i) => {
                if (trumpsObj.number === trumpNumber && i > 0 && i != array.length - 1) {
                    arrIndex = i - 1;
                } else if (trumpsObj.number === trumpNumber && i == 0) {
                    arrIndex = i;
                } else if (trumpsObj.number === trumpNumber && i == array.length - 1) {
                    arrIndex = i - 2;
                }
            })

            for (let i = 0; i < 3; i++) {
                newArr.push(array[arrIndex]);
                arrIndex++;
            }

            // Передаём в функцию объект трубы
            getDataTrump(newArr, array, trumpNumber, tehnic);
        }



    })
}

// Функция генерации страницы с трубой
function getDataTrump(array, baseArr, number, tehnic) {
    // СХЕМА
    const shemeMap = document.querySelector('.default-block_map .sheme__map');
    let trumpObjForm = {}; // Объект трубы
    shemeMap.innerHTML = '';
    // Рендер трубы в левой части страницы
    array.forEach(obj => {
        renderOneTrump(obj, shemeMap);
        if (obj.number === number) {
            for (key in obj) {
                trumpObjForm[key] = obj[key];
            }
        }
    })

    console.log(trumpObjForm)

    const trumps = shemeMap.querySelectorAll('.horizontal');
    let mainTrump;
    trumps.forEach(trump => {
        if (trump.querySelector('.number').innerHTML == number) {
            mainTrump = trump.parentElement.parentElement;
        } else {
            trump.parentElement.parentElement.style.opacity = '.5';
        }
    })
    mainTrump.style.maxWidth = '140px';
    mainTrump.style.marginLeft = '4px';
    mainTrump.style.marginRight = '4px';
    mainTrump.querySelector('.jumper-top').classList.add('peremichka_up');
    mainTrump.querySelector('.jumper-bottom').classList.add('peremichka_down');
    mainTrump.querySelector('.plug-ug').classList.add('zaglushka_ug');
    mainTrump.querySelector('.plug-sever').classList.add('zaglushka_sever');

    // ФОРМА

    // НОМЕР ТРУБЫ
    const trumpRadio = document.querySelector('[data-trump-number]');
    trumpRadio.querySelector('.radio-dropdown__label-text').innerHTML = trumpObjForm.number;

    //Добавляем список с трубами
    const radioDropdownTrumps = trumpRadio.querySelector('.radio-dropdown__radios');
    radioDropdownTrumps.innerHTML = '';
    baseArr.forEach(obj => {
        const trumpsItem = document.createElement('label');
        trumpsItem.classList.add('radio');

        trumpsItem.innerHTML = `
            <span class="radio__box radio__box_trump-number"></span>
            <span class="radio__label radio__box_trump-number_number">${obj.number}</span>
        `;
        radioDropdownTrumps.append(trumpsItem);

    });


    // ДЛИНА
    document.querySelector('[data-trump-dlina]').value = trumpObjForm.dlina;

    // СТАТУС
    const radiosStatus = document.querySelectorAll('[data-trump-status-item]');
    document.querySelector('[data-trump-status]').innerHTML = '';
    let status = 'Не определен';
    if (trumpObjForm.stage_works_id == null) {
        document.querySelector('[data-trump-status]').innerHTML = status;

        document.querySelector('[data-trump-status]').parentElement.className = '';
        document.querySelector('[data-trump-status]').parentElement.classList.add('radio-dropdown__label', 'input', 'stat-work0');
        radiosStatus[0].querySelector('.radio__input').checked = true;
    } else {
        status = radiosStatus[trumpObjForm.stage_works_id].querySelector('.radio__label').innerHTML;
        document.querySelector('[data-trump-status]').innerHTML = status;

        document.querySelector('[data-trump-status]').parentElement.className = '';
        document.querySelector('[data-trump-status]').parentElement.classList.add('radio-dropdown__label', 'input', `stat-work${trumpObjForm.stage_works_id}`);

        radiosStatus[trumpObjForm.stage_works_id].querySelector('.radio__input').checked = true;
    }
    // Меняем классы у инпута статус + труба
    radiosStatus.forEach((item, i) => {
        item.addEventListener('click', e => {
            if (e.target.closest('.radio')) {
                document.querySelector('[data-trump-status]').parentElement.className = '';
                document.querySelector('[data-trump-status]').parentElement.classList.add('radio-dropdown__label', 'input', `stat-work${i}`);

                mainTrump.className = '';
                mainTrump.classList.add('trump-wrap', `stat${i}`);

            }

        })
    });

    // ЗАГЛУШКИ/ПЕРЕМЫЧКИ
    if (trumpObjForm.zaglushka_sever === true) {
        document.querySelector('[data-zaglushka_sever]').checked = true;
    } else {
        document.querySelector('[data-zaglushka_sever]').checked = false;
    }
    if (trumpObjForm.zaglushka_ug === true) {
        document.querySelector('[data-zaglushka_ug]').checked = true;
    } else {
        document.querySelector('[data-zaglushka_ug]').checked = false;
    }
    if (trumpObjForm.peremichka_up === true) {
        document.querySelector('[data-peremichka_up]').checked = true;
    } else {
        document.querySelector('[data-peremichka_up]').checked = false;
    }
    if (trumpObjForm.peremichka_down === true) {
        document.querySelector('[data-peremichka_down]').checked = true;
    } else {
        document.querySelector('[data-peremichka_down]').checked = false;
    }

    // Подсчет выбранных checkbox
    const checkboxDropdown = document.querySelectorAll('.checkbox-dropdown');
    checkboxDropdown.forEach(dropdownItem => {
        const checkboxLabelText = dropdownItem.querySelector('.checkbox-dropdown__label-text'),
            radioInputs = dropdownItem.querySelectorAll('.checkbox__input');
        let countCheked = 0;
        checkboxLabelText.innerHTML = ' Не выбрано';
        radioInputs.forEach(radioInput => {
            if (radioInput.checked === true) {
                countCheked++;
                if (countCheked < 2 && countCheked > 0) {

                    radioInputs.forEach(radioInput => {
                        if (radioInput.checked === true) {
                            checkboxLabelText.innerHTML = radioInput.parentElement.querySelector('.checkbox__label').innerHTML;
                        }
                    })

                } else if (countCheked > 1) {
                    checkboxLabelText.innerHTML = `Выбрано: ${countCheked}`;
                } else {
                    checkboxLabelText.innerHTML = ' Не выбрано';
                }
            }
        });
        dropdownItem.addEventListener('click', e => {
            if (e.target.classList.contains('checkbox__input') && e.target.checked === true) {

                // Показываем заглушки и перемычки на схеме
                document.querySelector(`.${e.target.getAttribute('name')}`).classList.remove('hide');

                // Считаем кол-во выбранных
                countCheked++;

                if (countCheked < 2 && countCheked > 0) {

                    radioInputs.forEach(radioInput => {
                        if (radioInput.checked === true) {
                            checkboxLabelText.innerHTML = radioInput.parentElement.querySelector('.checkbox__label').innerHTML;
                        }
                    })

                } else if (countCheked > 1) {
                    checkboxLabelText.innerHTML = `Выбрано: ${countCheked}`;
                } else {
                    checkboxLabelText.innerHTML = ' Не выбрано';
                }

            } else if (e.target.classList.contains('checkbox__input') && e.target.checked === false && countCheked > 0) {
                countCheked--;

                if (countCheked < 2 && countCheked > 0) {

                    radioInputs.forEach(radioInput => {
                        if (radioInput.checked === true) {
                            checkboxLabelText.innerHTML = radioInput.parentElement.querySelector('.checkbox__label').innerHTML;
                        }
                    })

                } else if (countCheked > 1) {
                    checkboxLabelText.innerHTML = `Выбрано: ${countCheked}`;
                } else {
                    checkboxLabelText.innerHTML = ' Не выбрано';
                }

            }

            if (e.target.classList.contains('checkbox__input') && e.target.checked === false) {

                // Показываем заглушки и перемычки на схеме
                document.querySelector(`.${e.target.getAttribute('name')}`).classList.add('hide');
            }

        })
    });


    // ДЕФЕКТЫ
    let defectIndexCount;

    const arrDefObj = []; // Массив с объектами дефектов

    // Создаем 4 объекта с дефектами и пушим в массив
    for (let i = 1; i <= 4; i++) {
        let defObj = {};
        for (key in trumpObjForm) {
            defObj.number = trumpObjForm.number;
            if (key[4] == i && key.slice(0, 3) === 'def') {
                let keyModify = key.slice(0, 3) + key.slice(5); // Модифицируем ключ
                defObj[keyModify] = trumpObjForm[key] // Вносим пару ключ: значение в defObj
            };
        }
        arrDefObj.push(defObj);

    }

    // Рендерим дефекты на страницу
    const defectsContainer = document.querySelector('.defects-wrap__container');

    defectsContainer.innerHTML = '';
    arrDefObj.forEach((objDef, i) => {
        let defect = document.createElement('div');
        defect.classList.add('add-plot-repair__flex-container', 'add-plot-repair__defect');
        let defectIndex = i + 1;
        defect.id = `defect${defectIndex}`

        defect.innerHTML = `
        <div class="input-group input-group_medium">
            <span class="input-group__label">Характер дефекта</span>
            <div class="radio-dropdown dropdown">
                <div class="radio-dropdown__label input">
                    <span class="radio-dropdown__label-text">${objDef.def}</span>
                    <span class="radio-dropdown__label-icon">
                        <svg xmlns="http://www.w3.org/2000/svg"
                            viewBox="0 0 448 512">
                            <path
                                d="M224 416c-8.188 0-16.38-3.125-22.62-9.375l-192-192c-12.5-12.5-12.5-32.75 0-45.25s32.75-12.5 45.25 0L224 338.8l169.4-169.4c12.5-12.5 32.75-12.5 45.25 0s12.5 32.75 0 45.25l-192 192C240.4 412.9 232.2 416 224 416z">
                            </path>
                        </svg>
                    </span>
                </div>
                <div class="radio-dropdown__dropdown">

                    <span class="radio-dropdown__input-icon"></span>
                    <div class="radio-dropdown__radios">
                        <label class="radio">
                            <input type="radio" class="radio__input input"
                                name="def_${defectIndex}">
                            <span class="radio__box"></span>
                            <span class="radio__label">Не выбрано</span>
                        </label>
                        <label class="radio">
                            <input type="radio" class="radio__input input"
                                name="def_${defectIndex}">
                            <span class="radio__box"></span>
                            <span class="radio__label">Вмятина</span>
                        </label>
                        <label class="radio">
                            <input type="radio" class="radio__input input"
                                name="def_${defectIndex}">
                            <span class="radio__box"></span>
                            <span class="radio__label">ЗПТ</span>
                        </label>


                    </div>
                </div>
            </div>
        </div>
        <!-- Процент -->
        <div class="input-group input-group_small">
            <span class="input-group__label">Процент</span>
            <div class="input-wrap">
                <input type="text" class="input" value="${objDef.def_percent}" name="def_${defectIndex}_percent">
                <span class="input-wrap__label">%</span>
            </div>
        </div>
        <!-- Пикетаж -->
        <div class="input-group input-group_small">
            <span class="input-group__label">Пикетаж</span>
            <div class="input-wrap">
                <input type="text" class="input" value="${objDef.def_piket}" name="def_${defectIndex}_piket">
                <span class="input-wrap__label">км</span>
            </div>
        </div>
        <!-- Киломентраж -->
        <div class="input-group input-group_small">
            <span class="input-group__label">Киломентраж</span>
            <div class="input-wrap">
                <input type="text" class="input" value="${objDef.def_km}" name="def_${defectIndex}_km">
                <span class="input-wrap__label">км</span>
            </div>
        </div>
        <!-- Метод ремонта -->
        <div class="input-group input-group_medium" data-trump-type-remont>
            <span class="input-group__label">Метод ремонта</span>
            <div class="radio-dropdown dropdown">
                <div class="radio-dropdown__label input">
                    <span class="radio-dropdown__label-text">${objDef.def_type_rem}</span>
                    <span class="radio-dropdown__label-icon">
                        <svg xmlns="http://www.w3.org/2000/svg"
                            viewBox="0 0 448 512">
                            <path
                                d="M224 416c-8.188 0-16.38-3.125-22.62-9.375l-192-192c-12.5-12.5-12.5-32.75 0-45.25s32.75-12.5 45.25 0L224 338.8l169.4-169.4c12.5-12.5 32.75-12.5 45.25 0s12.5 32.75 0 45.25l-192 192C240.4 412.9 232.2 416 224 416z">
                            </path>
                        </svg>
                    </span>
                </div>
                <div class="radio-dropdown__dropdown">

                    <span class="radio-dropdown__input-icon"></span>
                    <div class="radio-dropdown__radios">
                        <label class="radio">
                            <input type="radio" class="radio__input input"
                                name="def_${defectIndex}_type_rem">
                            <span class="radio__box radio__box_trump-rem"></span>
                            <span class="radio__label">Не выбрано</span>
                        </label>
                        <label class="radio">
                            <input type="radio" class="radio__input input"
                                name="def_${defectIndex}_type_rem">
                            <span class="radio__box radio__box_trump-rem"></span>
                            <span class="radio__label">Шлифовка</span>
                        </label>
                        <label class="radio">
                            <input type="radio" class="radio__input input"
                                name="def_${defectIndex}_type_rem">
                            <span class="radio__box radio__box_trump-rem"></span>
                            <span class="radio__label">Вырезка (ЗК)</span>
                        </label>
                        <label class="radio">
                            <input type="radio" class="radio__input input"
                                name="def_${defectIndex}_type_rem">
                            <span class="radio__box radio__box_trump-rem"></span>
                            <span class="radio__label">Вырезка (ЗТ)</span>
                        </label>
                    </div>
                </div>
            </div>
        </div>
        <!-- Номер -->
        <div class="input-group input-group_small hide" data-trump-number>
            <span class="input-group__label">Номер</span>
            <div class="input-wrap input-wrap_left">
                <span class="input-wrap__label">№</span>
                <input type="text" class="input" value="${objDef.def_trump_number}"
                    name="def_${defectIndex}_number">
            </div>
        </div>
        <!-- Длина -->
        <div class="input-group input-group_small hide" data-trump-length>
            <span class="input-group__label">Длина</span>
            <div class="input-wrap">
                <input type="text" class="input" value="${objDef.def_trump_dlina}" name="def_${defectIndex}_dlina">
                <span class="input-wrap__label">мм</span>
            </div>
        </div>
        <a href="#" class="remove-btn">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512">
                <path
                    d="M432 256c0 17.7-14.3 32-32 32L48 288c-17.7 0-32-14.3-32-32s14.3-32 32-32l352 0c17.7 0 32 14.3 32 32z" />
            </svg>
        </a>
        `;
        defectsContainer.append(defect);
    });


    const defects = document.querySelectorAll('.add-plot-repair__defect'); // Получаем все дефекты в шаблоне

    function addImputs(defectOne) {
        const defectInput = defectOne.querySelector('[data-trump-type-remont] .radio-dropdown__label-text'),
            trumpLength = defectOne.querySelector('[data-trump-length]'),
            trumpnumber = defectOne.querySelector('[data-trump-number]');
        if (defectInput.innerText === 'Вырезка (ЗК)' || defectInput.innerText === 'Вырезка (ЗТ)') {
            trumpLength.classList.remove('hide');
            trumpnumber.classList.remove('hide');
            if (trumpLength.querySelector('.input').value === 'null' || trumpLength.querySelector('.input').value === 'undefined') {
                trumpLength.querySelector('.input').value = '';
            }
            if (trumpnumber.querySelector('.input').value === 'null' || trumpnumber.querySelector('.input').value === 'undefined') {
                trumpnumber.querySelector('.input').value = '';
            }
        } else {
            trumpLength.classList.add('hide');
            trumpnumber.classList.add('hide');
            trumpLength.querySelector('.input').value = '';
            trumpnumber.querySelector('.input').value = '';
        }

        if (defectOne.querySelector('.radio-dropdown__label-text').innerHTML === 'null') {
            defectOne.classList.add('hide')
        }
    }

    //  Перебор дефектов и добавление инпутов
    defects.forEach(defect => {
        addImputs(defect);
    });



    // Добавление инпута по клику
    document.addEventListener('click', e => {
        if (e.target.classList.contains('radio__box_trump-rem')) {
            addImputs(e.target.closest('.add-plot-repair__flex-container'));
        }
    })

    // Рендерим кнопку добавления дефекта на страниццу на страницу
    function addBtnDefInForm() {
        const addDefBtn = document.createElement('a');
        addDefBtn.classList.add('add-btn', 'add-btn-def');
        addDefBtn.href = '#';
        addDefBtn.innerHTML = `
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512">
                <path
                    d="M432 256c0 17.69-14.33 32.01-32 32.01H256v144c0 17.69-14.33 31.99-32 31.99s-32-14.3-32-31.99v-144H48c-17.67 0-32-14.32-32-32.01s14.33-31.99 32-31.99H192v-144c0-17.69 14.33-32.01 32-32.01s32 14.32 32 32.01v144h144C417.7 224 432 238.3 432 256z" />
            </svg>`;
        document.querySelector('[data-defects]').append(addDefBtn);
    }
    if (!document.querySelector('.add-btn-def')) {
        addBtnDefInForm()
    } else {
        document.querySelector('.add-btn-def').remove();
        addBtnDefInForm()
    }

    // Скрываем отсутствующие дефекты
    defects.forEach((defect, i) => {
        if (defect.querySelector('.radio-dropdown__label-text').innerHTML == 'undefined' || defect.querySelector('.radio-dropdown__label-text').innerHTML == 'null') {
            resetInput(defect, i);
            defect.classList.add('hide', 'add-plot-repair__defect_hide');
        }
        if (defect.querySelector('[data-trump-type-remont] .radio-dropdown__label-text').innerHTML == 'null') {
            defect.querySelector('[data-trump-type-remont] .radio-dropdown__label-text').innerHTML = 'Не выбрано'
        }

        //Удаление дефекта
        defect.querySelector('.remove-btn').addEventListener('click', e => {
            e.preventDefault();
            if (e.target.closest('.remove-btn')) {
                resetInput(defect, i);
                defect.classList.add('hide', 'add-plot-repair__defect_hide');
                defectIndexCount--;
                showAddBtn();
            }
        })

    });

    // Показ кнопки добавления дефекта
    const defectBlockAdd = document.querySelector('.add-btn-def');

    function showAddBtn() {
        if (defectIndexCount === 4) {
            defectBlockAdd.classList.add('hide')
        } else {
            defectBlockAdd.classList.remove('hide')
        }
    }
    showAddBtn();

    // Определянм кол-во дефектов которые уже есть на странице
    defectIndexCount = defects.length - document.querySelectorAll('.add-plot-repair__defect_hide').length;

    // Добавление нового дефекта по клику на кнопку
    defectBlockAdd.addEventListener('click', e => {
        e.preventDefault();

        const defectsHide = document.querySelectorAll('.add-plot-repair__defect_hide');

        addNewDeffectBlock(defectsHide[0]);
        defectIndexCount++;
        showAddBtn();
    })


    // Функция добавление нового дефекта
    function addNewDeffectBlock(defect) {
        defect.classList.remove('hide');
        defect.classList.remove('add-plot-repair__defect_hide');
    }


    //  Функция очищения Iтput
    function resetInput(defect, index) {
        let newDefectGropus = defect.querySelectorAll('.input-group');
        newDefectGropus.forEach(newDefectInputGroup => {
            // Очищаем все импуты
            let newDefectInput = newDefectInputGroup.querySelector('.input');
            newDefectInput.value = '';
            if (newDefectInput.name) {
                newDefectInput.name = `${newDefectInput.name.slice(0, -1)}${index + 1}` // Переписываем name у инпутов с учетом defectIndex 
            }
            // У выпадающих списков по умолчанию прописываем в label "Не выбрано"
            let newDefectLabelText = defect.querySelectorAll('.radio-dropdown__label-text');
            newDefectLabelText.forEach(label => {
                label.innerText = 'Не выбрано'
            })
        })
    };


    // ТЕХНИКА
    const tehnicWrap = document.querySelector('[data-tehnic-container]');
    tehnicWrap.innerHTML = '';
    tehnic.forEach(tehnicItem => {
        if (tehnicItem.location2 == trumpObjForm.id) {
            const tehnicForm = document.createElement('form');
            tehnicForm.classList.add('tehnic-form')
            tehnicForm.innerHTML = `
                <!-- Тип техники -->
                <div class="add-plot-repair__flex-container">
                    <div class="input-group input-group_medium">
                        <span class="input-group__label">Тип техники</span>
                        <div class="radio-dropdown dropdown">
                            <div class="radio-dropdown__label input">
                                <span class="radio-dropdown__label-text" data-tehnic-label>${tehnicItem.type}</span>
                                <span class="radio-dropdown__label-icon">
                                    <svg xmlns="http://www.w3.org/2000/svg"
                                        viewBox="0 0 448 512">
                                        <path
                                            d="M224 416c-8.188 0-16.38-3.125-22.62-9.375l-192-192c-12.5-12.5-12.5-32.75 0-45.25s32.75-12.5 45.25 0L224 338.8l169.4-169.4c12.5-12.5 32.75-12.5 45.25 0s12.5 32.75 0 45.25l-192 192C240.4 412.9 232.2 416 224 416z">
                                        </path>
                                    </svg>
                                </span>
                            </div>
                            <div class="radio-dropdown__dropdown">
                                <span class="radio-dropdown__input-icon"></span>
                                <div class="radio-dropdown__radios">
                                    <label class="radio tehnic-type">
                                        <input type="radio" class="radio__input input"
                                            name="type">
                                        <span class="radio__box"></span>
                                        <span class="radio__label" data-tehnic-type>Экскаватор</span>
                                    </label>
                                    <label class="radio tehnic-type">
                                        <input type="radio" class="radio__input input"
                                            name="type">
                                        <span class="radio__box"></span>
                                        <span class="radio__label">АРС</span>
                                    </label>
                                    <label class="radio tehnic-type">
                                        <input type="radio" class="radio__input input"
                                            name="type">
                                        <span class="radio__box"></span>
                                        <span class="radio__label">Трубоукладчик</span>
                                    </label>
                                    <label class="radio tehnic-type">
                                        <input type="radio" class="radio__input input"
                                            name="type">
                                        <span class="radio__box"></span>
                                        <span class="radio__label">Самосвал</span>
                                    </label>

                                </div>
                            </div>
                        </div>
                    </div>
                    <!-- Марка -->
                    <div class="input-group">
                        <span class="input-group__label">Марка</span>
                        <div class="radio-dropdown dropdown">
                            <div class="radio-dropdown__label input">
                                <span class="radio-dropdown__label-text">${tehnicItem.model}</span>
                                <span class="radio-dropdown__label-icon">
                                    <svg xmlns="http://www.w3.org/2000/svg"
                                        viewBox="0 0 448 512">
                                        <path
                                            d="M224 416c-8.188 0-16.38-3.125-22.62-9.375l-192-192c-12.5-12.5-12.5-32.75 0-45.25s32.75-12.5 45.25 0L224 338.8l169.4-169.4c12.5-12.5 32.75-12.5 45.25 0s12.5 32.75 0 45.25l-192 192C240.4 412.9 232.2 416 224 416z">
                                        </path>
                                    </svg>
                                </span>
                            </div>
                            <div class="radio-dropdown__dropdown">
                                <span class="radio-dropdown__input-icon"></span>
                                <div class="radio-dropdown__radios" data-tehnic-model></div>
                            </div>
                        </div>
                    </div>
                    <a href="#" class="remove-btn">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512">
                            <path
                                d="M432 256c0 17.7-14.3 32-32 32L48 288c-17.7 0-32-14.3-32-32s14.3-32 32-32l352 0c17.7 0 32 14.3 32 32z" />
                        </svg>
                    </a>
                </div>`;
            tehnicWrap.append(tehnicForm);
        }
    })

    // Формируем Закреплённый список техники
    const tehnicForms = document.querySelectorAll('.tehnic-form');

    tehnicForms.forEach(form => {
        const labelTehnic = form.querySelector('[data-tehnic-label]').innerHTML,
            tehnicModelList = form.querySelector('[data-tehnic-model]'),
            tehnicModelArr = [];

        tehnic.forEach(el => {
            if (el.type === labelTehnic) {
                tehnicModelArr.push(el)
            }
        });

        tehnicModelArr.forEach(obj => {
            appendModelItem(tehnicModelArr, tehnicModelList, obj)
        });

    });

    document.addEventListener('click', e => {
        if (e.target.closest('.tehnic-type')) {
            const labelTehnicClick = e.target.closest('.tehnic-type').querySelector('.radio__label').innerHTML,
                tehnicModelList = e.target.closest('.tehnic-type').closest('.tehnic-form').querySelector('[data-tehnic-model]'),
                tehnicModelLabelText = tehnicModelList.parentElement.parentElement.querySelector('.radio-dropdown__label-text'),
                tehnicModelArr = [];
            tehnicModelList.innerHTML = '';
            tehnicModelLabelText.innerHTML = 'Не выбрано';
            tehnic.forEach(el => {
                if (el.type === labelTehnicClick) {
                    tehnicModelArr.push(el)
                }
            });
            if( tehnicModelArr.length === 0 ) {
                appendModelItemNull(tehnicModelList);
            } else {
                tehnicModelArr.forEach(obj => {
                    appendModelItem(tehnicModelArr, tehnicModelList, obj)
                });
            }
            
        }
    })


    function appendModelItem(arr, parentConatiner, obj) {
        const tehnicItemLabel = document.createElement('label');
        tehnicItemLabel.classList.add('radio');
        tehnicItemLabel.innerHTML = `
        <input type="radio" class="radio__input input" name="Прописать">
        <span class="radio__box"></span>
        <span class="radio__label">${obj.model}</span>`;
        parentConatiner.append(tehnicItemLabel);
        
    }
    function appendModelItemNull(parentConatiner) {
        const tehnicItemLabel = document.createElement('label');
        tehnicItemLabel.classList.add('radio');
            tehnicItemLabel.innerHTML = 'Не найдена';
            parentConatiner.append(tehnicItemLabel);
        
    }







}





