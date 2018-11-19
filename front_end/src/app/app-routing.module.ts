import { Routes, RouterModule } from "@angular/router";
import { NgModule } from "@angular/core";
import { AuthGuard } from "./authentication/auth.guard";
import { LoginComponent } from "./login/login.component";
import { ChrompackComponent } from "./chrompack/chrompack.component";
import { SubjectComponent } from "./subject/subject.component";

const routes: Routes = [
    { path: '', redirectTo: 'chrompack', pathMatch: 'full' },
    { path: 'chrompack', component: ChrompackComponent, canActivate: [AuthGuard] },
    { path: 'chrompack/:id', component: ChrompackComponent, canActivate: [AuthGuard] },
    { path: 'subject/:id_chrompack', component: SubjectComponent, canActivate: [AuthGuard]},
    { path: 'login', component: LoginComponent }
];

@NgModule({
    imports: [RouterModule.forRoot(routes)],
    exports: [RouterModule]
})
export class AppRoutingModule { }
