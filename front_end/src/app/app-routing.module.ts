import { Routes, RouterModule } from "@angular/router";
import { NgModule } from "@angular/core";
import { AuthGuard } from "./authentication/auth.guard";
import { LoginComponent } from "./login/login.component";
import { PlateComponent } from "./plate/plate.component";

const routes: Routes = [
    { path: '', redirectTo: 'plate', pathMatch: 'full' },
    { path: 'plate', component: PlateComponent, canActivate: [AuthGuard] },
    { path: 'login', component: LoginComponent }
];

@NgModule({
    imports: [RouterModule.forRoot(routes)],
    exports: [RouterModule]
})
export class AppRoutingModule { }
