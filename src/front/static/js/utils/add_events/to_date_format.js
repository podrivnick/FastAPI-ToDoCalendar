async function formatDateTime(date, time, month, year) {
  const formattedMonth = month.toString().padStart(2, '0');
  const formattedDate =  date.toString().padStart(2, '0');

  // Разбираем время
  const [hours, minutes, period] = await time.split(/[:\s]/);
  let formattedHours = parseInt(hours, 10);

  // Корректируем часы в зависимости от AM/PM
  if (period === 'PM' && formattedHours !== 12) {
    formattedHours += 12;
  } else if (period === 'AM' && formattedHours === 12) {
    formattedHours = 0;
  }

  // Формируем строку времени в формате ISO
  const formattedTime = `${year}-${formattedMonth}-${formattedDate}T${formattedHours.toString().padStart(2, '0')}:${minutes.padStart(2, '0')}:00`;

  // Проверяем корректность формата даты
  const dateObj = await new Date(formattedTime);
  if (isNaN(dateObj.getTime())) {
    throw new RangeError('Invalid date or time value');
  }

  return dateObj.toISOString();
}


function splitTimeRange(timeRange) {
    const delimiter = ' - ';
    const times = timeRange.split(delimiter);

    if (times.length !== 2) {
        throw new Error("Invalid time range format");
    }

    const timeFrom = times[0].trim();
    const timeTo = times[1].trim();

    return { timeFrom, timeTo };
}