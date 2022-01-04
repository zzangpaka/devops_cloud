const zip = (...rows) => rows[0].map((_, column_index) => rows.map(row => row[column_index]));

const shuffle_array = (array) =>
    array.sort(() => Math.random() - Math.random());

export {
    zip,
    shuffle_array,
};
