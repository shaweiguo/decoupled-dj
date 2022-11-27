<template>
  <div class="container">
    <h2>Create a new invoice</h2>
    <form @submit.prevent="onSubmit">
      <div class="form">
        <div class="form__aside">
          <div class="form__field">
            <label for="user">Select a client</label>
            <select id="user" name="user" required>
              <option value="--">--</option>
              <option v-for="user in users" :key="user.email" :value="user.id">
                {{ user.name }} - {{ user.email }}
              </option>
            </select>
          </div>
          <div class="form__field">
            <label for="date">Date</label>
            <input id="date" name="date" type="date" required />
          </div>
          <div class="form__field">
            <label for="due_date">Due date</label>
            <input id="due_date" name="due_date" type="date" required />
          </div>
        </div>
        <div class="form__main">
          <div class="form__field">
            <label for="quantity">Qty</label>
            <input
              id="quantity"
              name="quantity"
              type="number"
              min="0"
              max="10"
              required
            />
          </div>
          <div class="form__field">
            <label for="description">Description</label>
            <input id="description" name="description" type="text" required />
          </div>
          <div class="form__field">
            <label for="price">Price</label>
            <input
              id="price"
              name="price"
              type="number"
              min="0"
              step="0.01"
              required
            />
          </div>
          <div class="form__field">
            <label for="taxed">Taxed</label>
            <input id="taxed" name="taxed" type="checkbox" />
          </div>
        </div>
        <div class="form__buttons">
          <button type="submit">Create invoice</button>
          <button disabled>Send email</button>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
export default {
  name: "InvoiceCreate",
  data: function () {
    return {
      users: [
        { id: 1, name: "xadrg", email: "adrg@acme.io" },
        { id: 2, name: "courg", email: "courg@zyx.dev" },
      ],
    };
  },
  methods: {
    onSubmit: function (e) {
      const formData = new FormData(e.target);
      const data = Object.fromEntries(formData);

      data.items = [
        {
            quantity: formData.get("quantity"),
            description: formData.get("description"),
            price: formData.get("price"),
            taxed: Boolean(formData.get("taxed")),
        },
      ];

      fetch("/billing/api/invoices/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data),
      })
        .then((res) => {
          if (!res.ok) throw Error(res.statusText);
          return res.json();
        })
        .then((res) => {
          console.log(res);
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  mounted() {
    fetch("/billing/api/clients/")
      .then((res) => {
        if (!res.ok) throw Error(res.statusText);
        return res.json();
      })
      .then((res) => {
        this.users = res;
      })
      .catch((err) => {
        console.log(err);
      });
  },
};
</script>
