function transformDataBack(data) {
    const baseDate = new Date(data.start_date); // Берем start_date как базовую дату
    const transformedData = {
        assigned_from: data.assigned_from,
        assigned_to: data.assigned_to,
        day: baseDate.getDate(),
        month: baseDate.getMonth() + 1, // В JS месяц начинается с 0, поэтому прибавляем 1
        year: baseDate.getFullYear(),
        events: [],
        id: data.id,
    };

    const event = {
        title: data.title,
        task: data.task,
        priority: data.priority.toString(),
        time: formatTime(data.start_date, data.due_date)
    };

    transformedData.events.push(event);

    return transformedData;
}

function formatTime(startDate, dueDate) {
    const start = new Date(startDate);
    const end = new Date(dueDate);

    const startHours = start.getHours() % 12 || 12;
    const startMinutes = start.getMinutes().toString().padStart(2, '0');
    const startPeriod = start.getHours() >= 12 ? 'PM' : 'AM';

    const endHours = end.getHours() % 12 || 12;
    const endMinutes = end.getMinutes().toString().padStart(2, '0');
    const endPeriod = end.getHours() >= 12 ? 'PM' : 'AM';

    return `${startHours}:${startMinutes} ${startPeriod} - ${endHours}:${endMinutes} ${endPeriod}`;
}
