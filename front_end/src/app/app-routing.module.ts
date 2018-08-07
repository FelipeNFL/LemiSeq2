import { Routes, RouterModule } from "@angular/router";
import { NgModule } from "@angular/core";
import { UploadComponent } from "./upload/upload.component";
import { AuthGuard } from "./authentication/auth.guard";
import { LoginComponent } from "./login/login.component";
import { PlateComponent } from "./plate/plate.component";

const routes: Routes = [
    { path: '', redirectTo: 'upload', pathMatch: 'full' },
    { path: 'plate/upload', component: UploadComponent, canActivate: [AuthGuard] },
    { path: 'plate', component: PlateComponent, canActivate: [AuthGuard] },
    { path: 'login', component: LoginComponent }
];

@NgModule({
    imports: [RouterModule.forRoot(routes)],
    exports: [RouterModule]
})
export class AppRoutingModule { }
