
local lpsPosition = Sensors.lpsPosition
local unpack = table.unpack

----------------------------------------
-- Блок объявления параметров полета ---
---------------------------------------------------------------------------------------------------------------------------------------------

-- Количество светодиодов 
-- Если есть модуль LED, то ledNumber = 29
local ledNumber = 4


-------------------------------------------------------------------


-----------------------------------------
-- Блок обработки работки светодиодов ---
---------------------------------------------------------------------------------------------------------------------------------------------

-- Упрощение вызова функции распаковки таблиц из модуля table



-- Создание порта управления светодиодами
local leds = Ledbar.new(ledNumber)

-- Функция смены цвета светодиодов
local function changeColor(r, g, b)
    -- Поочередное изменение цвета каждого из 4-х светодиодов
    for i=0, ledNumber - 1, 1 do
        leds:set(i, r, g, b)
    end
end 

-- Таблица цветов в формате RGB для передачи в функцию changeColor
local colors = {	red = 		{1, 0, 0},
					green = 	{0, 1, 0},
					blue = 		{0, 0, 1},
					purple = 	{0.5, 0, 0.5},
					cyan = 		{0, 0.5, 0.5},
					yellow = 	{0.5, 0.5, 0},
					white = 	{0.33, 0.33, 0.33},
					black = 	{0, 0, 0}
}


-------------------------------------------------------------------


-------------------------
-- Блок работы с uart ---
-------------------------

--  инициализируем Uart интерфейс
local uartNum = 4 -- номер Uart интерфейса (USART4)
local baudRate = 9600 -- скорость передачи данных
local dataBits = 8
local stopBits = 1
local parity = Uart.PARITY_NONE
local uart = Uart.new(uartNum, baudRate, parity, stopBits) --  создание протокола обмена

local message = {"A", "X", 0, "Y", 0, "Z", 0, "\n"}

-- отправляет текущие координаты
local function uart_send_message()
	lpsX, lpsY, lpsZ = lpsPosition()
	message[3] = lpsX
	message[5] = lpsY
	message[7] = lpsZ
	for i=1, 8, 1 do
        uart:write(message[i], string.len(message[i]))
    end
end

timer_uart = Timer.new(1, function() uart_send_message() end)
-------------------------------------------------------------------



----------------------------------------
-- Блок обработки движения по тчокам ---
---------------------------------------------------------------------------------------------------------------------------------------------
local copter = 1

local start_x_copter1 = 1.5
local start_y_copter1 = 1.5

local start_x_copter2 = 5.5
local start_y_copter2 = 5.5

local d_y = 0.5

local time_photo = 0.5

local z = 2

local points2 = {
        {5.5, start_y_copter2, z},
        
        {5.0, start_y_copter2, z}, -- 1
        {1.5, start_y_copter2 - d_y, z},
        
        {2.0, start_y_copter2 - d_y, z}, -- 2
        {5.5, start_y_copter2 - d_y * 2, z},
        
        {5.0, start_y_copter2 - d_y * 2, z}, -- 3
        {1.5, start_y_copter2 - d_y * 3, z},
        
        {2.0, start_y_copter2 - d_y * 3, z}, -- 4
		{5.5, start_y_copter2 - d_y * 3, z},
        
		{5.5, start_y_copter2, z},
        {5.5, start_y_copter2, 0}

}



-- Счетчик точек
local curr_point = 1

local function nextPoint()
	
	if (copter == 1) and (curr_point <= #points1) then
	
        Timer.callLater(1, function() ap.goToLocalPoint(unpack(points1[curr_point])) end)
		
	elseif (copter == 2) and (curr_point <= #points2) then
	
		Timer.callLater(1, function() ap.goToLocalPoint(unpack(points2[curr_point])) end)
	else
		timer_uart:stop()
        Timer.callLater(1, function() ap.push(Ev.MCE_LANDING) end)
    end
	 
	curr_point = curr_point + 1
	
end

-------------------------------------------------------------------



-- Функция обработки событий, автоматически вызывается автопилотом
function callback(event)
    -- Когда коптер поднялся на высоту взлета Flight_com_takeoffAlt, переходим к полету по точкам
    if(event == Ev.TAKEOFF_COMPLETE) then
		timer_uart:start()
        Timer.callLater(0.5 , function() nextPoint() end)
    end
    
	-- Когда коптер достиг текущей точки, переходим к следующей
    if(event == Ev.POINT_REACHED) then
        Timer.callLater(0.5 , function() nextPoint() end)
    end
    
	-- Когда коптер приземлился, выключаем светодиоды
    if (event == Ev.COPTER_LANDED) then
        changeColor(table.unpack(colors.black))
    end
end


-- Старт полета с пульта
function start()
	local _,_,_,_,_,ch6,_,ch8 = Sensors.rc() -- SWD and SWA
	if ch6 < 1 and ch8 > 0 then
	    changeColor(table.unpack(colors.white))
	    -- Предстартовая подготовка
        ap.push(Ev.MCE_PREFLIGHT)

	    -- Таймер, через 2 секунды вызывающий функцию взлета
        Timer.callLater(2, function() ap.push(Ev.MCE_TAKEOFF) end)
	
	else
		changeColor(table.unpack(colors.black))
		Timer.callLater(0.2, function() start() end)
	    
	end

end

start()
