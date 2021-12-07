import { Outlet, Link } from "react-router-dom";
import {  Route } from "react-router-dom";
// // material-ui
// import Navbar from "./navbarko/Navbar";
// tailwind-css
import NavbarTcss from "./navbarko/NavbarTcss";
import Crud from "./routes/product/productcrud";


export default function App() {
  return (
    <div>
      <NavbarTcss />
        <Link to="/invoices">Invoices</Link> |{" "}
        <Link to="/expenses">Expenses</Link>
 {/*       <Route path="/crud" element={<Crud />}>
        </Route>*/}
      <Outlet />
    </div>
  );
}