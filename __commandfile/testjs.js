function app() {
    return {
        month: '',
        year: '',
        no_of_days: [],
        blankdays: [],

        initDate() {
            let today = new Date(2010, 1, 13,);
            this.month = today.getMonth();
            this.year = today.getFullYear();
            this.datepickerValue = new Date(this.year, this.month, today.getDate()).toDateString();
            // console.log(this.datepickerValue)
            // console.log(new Date(today))
        // initDate()
            },

    }
}

a = app()
a.initDate()

console.log(a)

// >>> output
// {
//   month: 0,
//   year: 2022,
//   no_of_days: [],
//   blankdays: [],
//   initDate: [Function: initDate],
//   datepickerValue: 'Sat Jan 01 2022'
// }