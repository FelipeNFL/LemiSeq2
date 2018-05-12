import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';


import { AppComponent } from './app-component/app.component';
import { HeaderComponent } from './header/header.component' 
import { appRoutes } from './routes';
import { RouterModule } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { RootComponent } from './root/root.component';
// import { AuthService } from './service/auth.service';

@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    LoginComponent,
    RootComponent
  ],
  imports: [
    BrowserModule,
    RouterModule.forRoot(appRoutes)
  ],
  providers: [
    // AuthService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
