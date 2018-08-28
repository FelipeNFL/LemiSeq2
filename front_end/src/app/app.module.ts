import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';

import { AppComponent } from './app-component/app.component';
import { HeaderComponent } from './header/header.component' 
import { LoginComponent } from './login/login.component';
import { UploadComponent } from './upload/upload.component';
import { LoaderComponent } from './loader/loader.component';
import { FooterComponent } from './footer/footer.component';
import { PlateComponent } from './plate/plate.component';
import { SlotsViewComponent } from './slots-view/slots-view.component';
import { ChrompackListComponent } from './chrompack-list/chrompack-list.component';
import { SubjectListComponent } from './subject-list/subject-list.component';

import { AuthService } from './services/auth.service';
import { ChromPackService } from './services/chrompack.service';
import { AuthGuard } from './authentication/auth.guard';
import { AuthInterceptor } from './authentication/auth-interceptor';
import { UserService } from './services/user.service';
import { ChrompackServiceObservable } from './services/chrompack-observable.service';
import { SubjectService } from './services/subject.service';

@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    LoginComponent,
    UploadComponent,
    LoaderComponent,
    FooterComponent,
    PlateComponent,
    SlotsViewComponent,
    ChrompackListComponent,
    SubjectListComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    FormsModule,
    AppRoutingModule,
    NgbModule.forRoot()
  ],
  bootstrap: [AppComponent],
  providers: [
    ChromPackService,
    ChrompackServiceObservable,
    SubjectService,
    UserService,
    AuthService,
    AuthGuard,
    {
      provide: HTTP_INTERCEPTORS,
      useClass: AuthInterceptor,
      multi: true,
    },
  ],
  entryComponents: [
    UploadComponent
  ]
})
export class AppModule { }
