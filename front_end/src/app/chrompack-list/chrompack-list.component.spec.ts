import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ChrompackListComponent } from './chrompack-list.component';

describe('SlotsListComponent', () => {
  let component: ChrompackListComponent;
  let fixture: ComponentFixture<ChrompackListComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ChrompackListComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ChrompackListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
