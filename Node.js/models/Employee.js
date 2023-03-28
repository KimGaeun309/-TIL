const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const mongoosePaginate = require('mongoose-paginate-v2'); // 추가

// declare employee's schema
// mongoose's schema type : https://mongoosejs.com/docs/schematypes.html
const employeeSchema = new Schema(
  {
    name: {
      type: String,
    },
    designation: {
      type: String,
    },
    email: {
      type: String,
    },
    phone: {
      type: String,
    },
    age: {
      type: Number,
    },
    avatar: {
      // 파일 업로드를 위한
      type: String,
    },
  },
  { timestamps: true }
);
// 'timestamps: true' => 데이터베이스에 created_at, updated_at을 자동 생성
// 단, 표준 시간이 한국보다 9시간 빠르다.

employeeSchema.plugin(mongoosePaginate); // 추가

const Employee = mongoose.model('Employee', employeeSchema);
module.exports = Employee;
// our model is ready to use
