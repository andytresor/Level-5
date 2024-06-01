const { Schema, model } = require('mongoose');

const userSchema = new Schema ({
    email: { type: String, require: true },
    username: { type: String, require: true },
    description: { type: String, require: true },
    create_at: { type: Date, default: Date.now}
});

const User = model('user', userSchema);

module.exports = User