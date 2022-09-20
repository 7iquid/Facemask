import { render } from "react-dom";
import { Outlet } from "react-router-dom";
import {
  BrowserRouter,
  Routes,
  Route
} from "react-router-dom";
import App from "./App";

import Expenses from "./routes/expenses";
import Invoices from "./routes/invoices";
import Login from "./routes/account/login";


const rootElement = document.getElementById("root");
render(
  <BrowserRouter>
    <Routes>
      <Route path="/" element={<App />}>
        <Route path="expenses" element={<Expenses />} />
        <Route path="invoices" element={<Invoices />} />
        <Route path="login" element={<Login />} />
        <Route path="*" element={<NotHanap />} />
      </Route>
  
    </Routes>
  </BrowserRouter>,
  rootElement
);


export default function NotHanap() {

  return (
    <main>testing start</main>
  );
}