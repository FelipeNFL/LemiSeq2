import { Routes } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { AppComponent } from './app-component/app.component';

export const appRoutes: Routes = [
    { path: 'login', component: LoginComponent},
    { path: '', component: AppComponent}
]